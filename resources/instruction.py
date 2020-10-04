from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.instruction import Instruction, instruction_list


class InstructionListResource(Resource):

    def get(self):
        data = []
        for instruction in instruction_list:
            if instruction.is_publish is True:
                data.append(instruction.data)
        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        instruction = Instruction(name=data['name'], steps=data['steps'])
        instruction_list.append(instruction)
        return instruction.data, HTTPStatus.CREATED


class InstructionResource(Resource):

    def get(self, instruction_id):
        return instruction_list[instruction_id-1].data

    def put(self, instruction_id):

        data = request.get_json()
        instruction = Instruction(name=data['name'], steps=data['steps'])
        instruction_list[instruction_id+1] = instruction
        return instruction.data, HTTPStatus.OK

    def delete(self, instruction_id):
        instruction_list.pop(instruction_id-1)
        return HTTPStatus.OK


class InstructionPublish(Resource):
    def put(self, instruction_id):
        instruction = next(Instruction for instruction in instruction_list if instruction.id == instruction_list)
        if instruction is None:
            return{'message': 'Instruction not found'}, HTTPStatus.NOT_FOUND

        instruction.is_publish = True

        return {}, HTTPStatus.NO_CONTENT


class InstructionUnpublish(Resource):
    def delete(self, instruction_id):
        instruction = next(Instruction for instruction in instruction_list if instruction.id == instruction_list)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND



        return {}, HTTPStatus.NO_CONTENT
