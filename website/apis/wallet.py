import shelve

from .. import DB_WALLET_LOCATION
from ..models import Wallet
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('owner_uid', type=str, required=True)

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
