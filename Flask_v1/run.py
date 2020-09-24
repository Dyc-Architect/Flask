from app import factory
from flask import jsonify
import yaml
from app.code import ResponseCode
from app.response import ResMsg

app = factory.create_app(config_name='DEVELOPMENT')

with open("config/msg.yaml", encoding="utf-8") as f:
    msg_conf = yaml.safe_load(f)
app.config.update(msg_conf)


@app.route("/", methods=["GET"])
def test():
    res = ResMsg()
    test_dict = dict(name="Du", age=18)
    res.update(code=ResponseCode.SUCCESS, data=test_dict)
    return jsonify(res.data)


if __name__ == "__main__":
    app.run()
