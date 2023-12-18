# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
from pymongo import MongoClient
import couponmanage_pb2_grpc
import couponmanage_pb2
import logging
import grpc


class CouponManager(couponmanage_pb2_grpc.CouponManagerServicer):
    def __init__(self):
        conn = MongoClient(host="127.0.0.1", port=27017)
        db = conn.coupon_manager
        self.cafe_collection = db.cafe_collection
        self.user_collection = db.user_collection
        self.user_id_counter = db.counters

    def ReceiveAllCafes(self, request, context):
        # self.user_id_counter.update_one(
        #     {"key": "userid"},
        #     {"$inc": {"seq": 1}}
        # )
        # user_id = self.user_id_counter.find_one({"key": "userid"})["seq"]
        # self.user_collection.update_one(
        #     {"name": "조상현"},
        #     {"$set": {"user_id": user_id}}
        # )

        data = list(self.cafe_collection.find({}, {"_id":False}))
        return couponmanage_pb2.AllCafeReply(cafes=data)

    def ReceiveCafeDetail(self, request, context):
        data = self.cafe_collection.find_one({"name": request.name}, {"_id":False})
        return couponmanage_pb2.CafeDetail(
            name=data["name"],
            address=data["address"],
            rating=data["rating"],
            operating_info=data["operating_info"]
        ) if data else couponmanage_pb2.CafeDetail()

    def RegisterCafe(self, request, context):
        if self.cafe_collection.find_one({"name": request.name}) is not None:
            return couponmanage_pb2.CUDReply(is_success=False)

        data = {}
        data["name"] = request.name
        data["address"] = request.address
        data["rating"] = request.rating
        data["operating_info"] = []
        for item in request.operating_info:
            operating_data = {}
            operating_data["open_day_of_the_week"] = item.open_day_of_the_week
            operating_data["open_hour"] = item.open_hour
            operating_data["close_day_of_the_week"] = item.close_day_of_the_week
            operating_data["close_hour"] = item.close_hour
            data["operating_info"].append(operating_data)
        data["operating_info"].sort(key=lambda x: x["open_day_of_the_week"])

        self.cafe_collection.insert_one(data)
        return couponmanage_pb2.CUDReply(is_success=True)

    def UpdateCafe(self, request, context):
        if self.cafe_collection.find_one({"name": request.name}) is None:
            return couponmanage_pb2.CUDReply(is_success=False)

        data = {}
        if not request.is_address_null:
            data["address"] = request.address
        if not request.is_rating_null:
            data["rating"] = request.rating
        if not request.is_operating_info_null:
            data["operating_info"] = []
            for item in request.operating_info:
                operating_data = {}
                operating_data["open_day_of_the_week"] = item.open_day_of_the_week
                operating_data["open_hour"] = item.open_hour
                operating_data["close_day_of_the_week"] = item.close_day_of_the_week
                operating_data["close_hour"] = item.close_hour
                data["operating_info"].append(operating_data)
            data["operating_info"].sort(key=lambda x: x["open_day_of_the_week"])

        self.cafe_collection.update_one(
            {"name": request.name},
            {"$set": data}
        )

        return couponmanage_pb2.CUDReply(is_success=True)

    def DeleteCafe(self, request, context):
        if self.cafe_collection.find_one({"name": request.name}) is None:
            return couponmanage_pb2.CUDReply(is_success=False)

        self.cafe_collection.delete_one({"name": request.name})
        return couponmanage_pb2.CUDReply(is_success=True)

    def ReceiveAllCoupons(self, request, context):
        user_id = request.user_id
        user = self.user_collection.find_one({"user_id": user_id}, {"_id":False})
        if user is None:
            return couponmanage_pb2.AllCouponReply(is_success=False)
        return couponmanage_pb2.AllCouponReply(is_success=True, coupons=user["coupon"])

    def ReceiveCouponDetail(self, request, context):
        user_id = request.user_id
        cafe_name = request.cafe_name
        user = self.user_collection.find_one({"user_id": user_id}, {"_id": False})
        cafe = self.cafe_collection.find_one({"name": cafe_name}, {"_id": False})

        if user is None or cafe is None:
            return couponmanage_pb2.CouponDetailReply(is_success=False)

        for coupon_data in user["coupon"]:
            if coupon_data["cafe_name"] == cafe_name:
                print
                return couponmanage_pb2.CouponDetailReply(
                    is_success=True, coupon_detail=coupon_data)
        return couponmanage_pb2.CouponDetailReply(is_success=True)

    def IncreaseCoupon(self, request, context):
        user_id = request.user_id
        cafe_name = request.cafe_name
        user = self.user_collection.find_one({"user_id": user_id}, {"_id": False})
        cafe = self.cafe_collection.find_one({"name": cafe_name}, {"_id": False})

        if user is None or cafe is None:
            return couponmanage_pb2.CUDReply(is_success=False)

        for coupon_data in user["coupon"]:
            if coupon_data["cafe_name"] == cafe_name:
                self.user_collection.update_one(
                    {
                        "user_id": user_id,
                        "coupon.cafe_name": cafe_name
                    },
                    {"$inc": {"coupon.$.count": 1}}
                )
            break
        else:
            self.user_collection.update_one(
                {"user_id": user_id},
                {"$push": {"coupon": {
                    "cafe_name": cafe_name,
                    "count": 1
                }}}
            )
        return couponmanage_pb2.CUDReply(is_success=True)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    couponmanage_pb2_grpc.add_CouponManagerServicer_to_server(CouponManager(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()