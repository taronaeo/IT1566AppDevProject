import shelve

from .. import DB_WALLET_LOCATION
from ..models import Wallet
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('owner_uid', type=str, required=True)
parser.add_argument('balance', type=float, required = False)
parser.add_argument('stamps_collected', type=int, required = False)
parser.add_argument('transactions', type=str, required = False) #!Added extra arguments for the other parameters in the wallet model

class WalletApiEndpoint(Resource):
  def get(self, owner_uid):
    with shelve.open(DB_WALLET_LOCATION) as db:
      try:
        return db[owner_uid].__dict__
      except KeyError:
        return { "message": "Wallet not found." }, 404

  def post(self):
    args = parser.parse_args()

    with shelve.open(DB_WALLET_LOCATION) as db:
      try:
        if args['owner_uid'] in db:
          return { "message": "Wallet already exists." }, 409

        wallet = Wallet(args['owner_uid'], 0, 0, [])
        db[args['owner_uid']] = wallet
        return wallet.__dict__
      except Exception:
        return { "message": "Something went wrong." }, 500

    def put(self,owner_uid):
      args = parser.parse_args()
      with shelve.open(DB_WALLET_LOCATION) as db:
        try:
          exists = db[owner_uid]
          if exists:
            exists = Wallet(
              args['owner_uid'],
              args['balance'],
              args['stamps_collected'],
              args['transactions']
            )
            db[owner_uid] = exists
            return exists.__dict__
        except KeyError:
          return {'code': 404, 'message': 'Wallet not found'}, 404
        except Exception:
          return {"code": 500, "message": "Something went wrong."}, 500
      
    def delete(self,owner_uid):
      with shelve.open(DB_WALLET_LOCATION) as db:
        try:
          exists = db[owner_uid]
          if exists:
              del db[owner_uid]
              return {'code': 200, 'message': 'Wallet Deleted'}, 200
        except KeyError:
          return {'code': 404, 'message': 'Wallet not found'}, 404
        except Exception: 
          return {'code': 500, 'message': 'Somthing went wrong'}, 500

