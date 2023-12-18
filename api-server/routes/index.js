var express = require('express');
var router = express.Router();

const PROTO_PATH = __dirname + "/../protos/couponmanage.proto";
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const packageDefinition = protoLoader.loadSync(
  PROTO_PATH,
  {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  });
const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const routes = protoDescriptor.couponmanage;

let client = new routes.CouponManager('localhost:50051', grpc.credentials.createInsecure());

/* receive all cafe data. */
router.get('/cafes', function(req, res) {
  client.receiveAllCafes({}, function(err, response) {
    if (err == null) {
      res.status(200).json(JSON.stringify(response));
    } else {
      res.sendStatus(500);
    }
  });
});

/* receive cafe data by cafe name. */
router.get('/cafes/:cafeName', function(req, res) {
  const cafeName = req.params.cafeName;
  client.receiveCafeDetail({name: cafeName}, function(err, response) {
    if (err == null) {
      if (response.name != "") {
        res.status(200).json(JSON.stringify(response));
      } else {
        res.sendStatus(404);
      }
    } else {
      res.sendStatus(500);
    }
  });
});

/* Insert new cafe data */
router.post('/cafes', function(req, res){
  const {name, address, rating, operating_info} = req.body;
  
  client.registerCafe(
    {
      name: name,
      address: address,
      rating: rating,
      operating_info: operating_info,
    },
    function(err, response) {
      if (err == null) {
        console.log(response);
        if (response?.is_success == true) {
          res.sendStatus(201);
        } else {
          res.status(409).json({error: `${name} already exists`});
        }
      } else {
        res.sendStatus(500);
      }
    }
  );
 });

 /* Update cafe data */
 router.patch('/cafes/:cafeName', function(req, res){
  const cafeName = req.params.cafeName;
  const {address, rating, operating_info} = req.body;
  
  client.updateCafe(
    {
      name: cafeName,
      address: address,
      rating: rating,
      operating_info: operating_info ? operating_info : null,
      is_address_null: address ? false : true,
      is_rating_null: rating ? false : true,
      is_operating_info_null: operating_info ? false : true,
    },
    function(err, response) {
      if (err == null) {
        console.log(response);
        if (response?.is_success == true) {
          res.sendStatus(204);
        } else {
          res.sendStatus(404);
        }
      } else {
        res.sendStatus(500);
      }
    }
  );
 });

 /* delete cafe data. */
router.delete('/cafes/:cafeName', function(req, res) {
  const cafeName = req.params.cafeName;
  client.deleteCafe({name: cafeName}, function(err, response) {
    if (err == null) {
      if (response?.is_success) {
        res.sendStatus(204);
      } else {
        res.sendStatus(404);
      }
    } else {
      res.sendStatus(500);
    }
  });
});

 /* receive specific user`s all coupons */
 router.get('/users/:userId/coupons', function(req, res) {
  const userId = req.params.userId;
  client.receiveAllCoupons({user_id: userId}, function(err, response) {
    if (err == null) {
      if (response?.is_success) {
        res.status(200).json(JSON.stringify(response));
      } else {
        console.log(response)
        res.sendStatus(404);
      }
    } else {
      res.sendStatus(500);
    }
  });
});

 /* increase user`s coupon */
 router.post('/users/:userId/coupons/:cafeName', function(req, res) {
  const userId = req.params.userId;
  const cafeName = req.params.cafeName;
  
  client.increaseCoupon(
    {
      user_id: userId,
      cafe_name: cafeName,
    },
    function(err, response) {
      if (err == null) {
        if (response?.is_success) {
          res.sendStatus(204);
        } else {
          res.sendStatus(404);
        }
      } else {
        res.sendStatus(500);
      }
    }
  );
});

module.exports = router;