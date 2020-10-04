from flask import Flask, jsonify, request
from flask_restful import Api
from http import HTTPStatus

from resources.instruction import InstructionListResource, InstructionResource, InstructionPublish, InstructionUnpublish

app = Flask(__name__)
api = Api(app)


api.add_resource(InstructionListResource, '/instructions')
api.add_resource(InstructionResource, '/instructions/<int:instruction_id>')
api.add_resource(InstructionPublish, '/instructions/<int:instruction_id>/publish')
api.add_resource(InstructionUnpublish, "/instructions/<int:instruction_id>/Unpublished")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
