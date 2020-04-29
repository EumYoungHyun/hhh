import React from "react";
import { useHistory, Link } from "react-router-dom";
import { Form, Input, Button } from "antd";
import "./Login.scss";
import axios from "axios";
import Header from "../common/Header";

const loginURL = `http://13.125.113.171:8000/login/`;

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 8,
  },
};
const tailLayout = {
  wrapperCol: {
    offset: 13,
    span: 16,
  },
};

const Login = () => {
  let history = useHistory();

  const onFinish = async (values) => {
    const resultURL = loginURL + `${values.username}/${values.password}`;
    let form_data = new FormData();
    form_data.append("username", values.username);
    form_data.append("password", values.password);
    await axios
      .get(resultURL, form_data, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((resp) => {
        if (resp.status === 200) {
          console.log(resp.data.user);
          sessionStorage.setItem("username", values.username);
          sessionStorage.setItem("user", resp.data.user);
          sessionStorage.setItem("id", resp.data.user.id);
          sessionStorage.setItem("avatar", resp.data.user.avatar)
          history.push("/");
        }
      });
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <>
      <Header />
      <br />
      <div className="loginForm">
        <Form
          {...layout}
          name="basic"
          initialValues={{
            remember: true,
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
        >
          <Form.Item
            label="아이디"
            name="username"
            rules={[
              {
                required: true,
                message: "Please input your username!",
              },
            ]}
          >
            <Input id="username" />
          </Form.Item>

          <Form.Item
            label="비밀번호"
            name="password"
            rules={[
              {
                required: true,
                message: "Please input your password!",
              },
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item {...tailLayout}>
            <Button htmlType="submit">로그인</Button>
            &nbsp;
            <Link to="/register">회원가입 하러가기</Link>
          </Form.Item>
        </Form>
      </div>
    </>
  );
};

export default Login;
