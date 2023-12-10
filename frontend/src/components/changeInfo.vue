<template>
  <div class="personinfo">
    <div id="upperimage">
    </div>
    <div id="placeholder">
      <p class="info">点击修改背景</p>
    </div>
    <p id="changeavatar">点击修改头像</p>
    <a-avatar id="avatar" shape="square" :size="128" icon="user" />
    <h1 id="username">点击修改ID</h1>
    <input id="sign" value="修改个人简介"></input>
    <div id="buttongroup">
      <a-button id="changeconfirm" type="primary" @click="emitConfirm">确定修改</a-button>
      <a-button id="changereturn" type="danger" @click="emitReturn">返回</a-button>
    </div>
  </div>
</template>

<script>
  function getBase64(img, callback) {
    const reader = new FileReader();
    reader.addEventListener('load', () => callback(reader.result));
    reader.readAsDataURL(img);
  }
  export default {
    name: "changeInfo",
    data() {
      return {
        loading: false,
        imageUrl: '',
      }
    },
    methods: {
      emitReturn: function () {
        console.log('Return button on change info page clicked')
        this.$emit('clickReturn')
      },
      emitConfirm: function () {
        console.log('Confirm button on change info page clicked')
        this.$emit('clickConfirm')
      },

    }
  }
</script>

<style scoped>
  .personinfo {
    position: relative;
    width: 67%;
    height: 300px;
    margin: 15px auto 0;
    background-color: aliceblue;
  }
  #upperimage {
    height: 200px;
    width: 100%;
    text-align: center;
    background-image: url("../assets/info.jpg");
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
    position: absolute;
    opacity: 0.5;
    z-index: 20;
  }
  #placeholder {
    height: 200px;
    width: 100%;
    z-index: 30;
    text-align: center;
    position: absolute;
    display: flex;
  }
  .info {
    horiz-align: center;
    margin: auto;
    z-index: 30;
    font-size: 30px;
  }
  #avatar {
    position: absolute;
    bottom: 15px;
    left: 15px;
    z-index: 30;
  }
  #username {
    position: absolute;
    margin: 200px auto 0 180px;
    font-size: 35px;
  }
  #sign {
    position: absolute;
    margin: 250px auto 0 180px;
  }
  #changeavatar {
    position: absolute;
    margin: 210px auto 0 37px;
    z-index: 40;
  }
  #buttongroup {
    position: absolute;
    right: 0;
    bottom: 0;
    margin-right: 10px;
    margin-bottom: 10px;
  }
  #changeconfirm {
    float: left;
    margin-right: 10px;
  }
  #changereturn {
    float: left;
  }
</style>
