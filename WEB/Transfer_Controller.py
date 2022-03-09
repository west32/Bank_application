from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from Service import Money_Transfer_Usecase
from Service.Money_Transfer_Command import MoneyTransferCommand, MoneyTransferCommandException
from WEB.Transfer_Request import TransferRequest


transfers = Blueprint('transfers', __name__)


@transfers.post('/transfers')
def transfer():
    transfer_request = TransferRequest()
    json = request.get_json()
    try:
        result = transfer_request.load(json)
        use_case = Money_Transfer_Usecase.MoneyTransferUseCase()
        command_a = MoneyTransferCommand(result["a_account"], result["b_account"], result["money_amount"])
        use_case.transfer(command_a)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except MoneyTransferCommandException as err:
        return jsonify({"message": err.message}), 400

    return "wszystko git ziom", 200


