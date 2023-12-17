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
      let jsonObject = response.cafes.toObject();
      res.status(200).json(JSON.stringify(response));
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

module.exports = router;