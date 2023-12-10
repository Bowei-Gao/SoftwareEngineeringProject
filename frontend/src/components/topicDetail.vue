<template>
    <div class="topic">
      <div class="content">
        <a-avatar shape="square" size="large" icon="user" id="topicavatar"/>
        <h2 id="topicuser">ID</h2>
        <a-button type="link" id="topicdelete">
          删除
        </a-button>
        <div class="texts">
          <h1 id="topictitle">Lorem ipsum</h1>
          <p id="topiccontent">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          <a-card hoverable style="width: 240px">
            <img
              slot="cover"
              alt="example"
              src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
            />
          </a-card>
          <p id="topictime">2020/05/05 15:44</p>
        </div>
        <div id="topictags">
          <a-tag>
            Tag 1
          </a-tag>
          <a-tag>
            Tag 2
          </a-tag>
        </div>
        <a-button type="link" id="topicreport">
          举报
        </a-button>
      </div>
      <a-divider id="div1" orientation="left">评论区</a-divider>
      <div id="btndiv1"><a-button type="primary" id="writecomment">写评论</a-button></div>

    </div>
</template>

<script>
    export default {
        name: "topicDetail.vue",

    }
</script>

<style scoped>
.topic {
  position: relative;
  width: 40%;
  margin: 15px auto;
  border: darkgrey solid 2px;
  border-radius: 5px;
}
  #topicavatar {
    margin: 15px;
    display: inline-block;
  }
  #topicuser {
    margin: 15px 0;
    display: inline-block;
  }
  #topicdelete {
    color: gray;
    position: absolute;
    right: 0;
    top: 0;
    margin-top: 15px;
    margin-right: 15px;
  }
  .texts {
    margin-left: 15px;
    margin-right: 30px;
    margin-bottom: 15px;
  }
  #topictags  {
    margin-left: 15px;
    float: left;
    margin-bottom: 15px;
  }
  #topicreport {
    color: red;
    margin-right: 15px;
    float: right;
    margin-bottom: 15px;
  }
  #writecomment {
    margin: 0 auto;
  }
  #btndiv1 {
    text-align: center;
    margin-bottom: 15px;
  }
</style>
