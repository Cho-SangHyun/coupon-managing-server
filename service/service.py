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
        self.coupon_collection = db.coupon_collection

    def RegisterCafe(self, request, context):
        if self.cafe_collection.find_one({"name": request.name}) is not None:
            return couponmanage_pb2.CafeRegisterReply(is_success=False)

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
        return couponmanage_pb2.CafeRegisterReply(is_success=True)


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