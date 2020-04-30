import React from "react";
import { Link } from "react-router-dom";
import Feed from "./feed/Feed";
import UserCard from "./userCard/userCard";
import "./FeedList.scss";
import axios from "axios";

class FeedList extends React.Component {
  state = {
    userId: 0,
    userName: sessionStorage.getItem("username"),
    userAvatar: "",
    feedList: [],
    feedNum: 0,
  };

  async componentDidMount() {
    await axios
      .get("http://13.125.113.171:8000/feedlist/user/" + this.state.userName)
      .then((res) => {
        this.setState({
          ...this.state,
          userId: res.data[0].writer_id,
          userAvatar: res.data[0].avatar,
          feedList: res.data,
          feedNum: res.data.length,
        });

        console.log(this.state);
      });
  }

  render() {
    return (
      <div id="feed-list">
        <UserCard
          avatarPic={this.state.userAvatar}
          userId={this.state.userId}
          feedNum={this.state.feedNum}
        />

        <input type="text" id="search-bar" placeholder="검색"></input>
        <div id="list">
          <div className="row">
            {this.state.feedList.map((data: any) => (
              <Link to="feedDetail">
                <Feed url={data.photos[0]}></Feed>
              </Link>
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default FeedList;
