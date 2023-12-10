<template>
    <div class="personinfo">
      <div id="upperimage">

      </div>
      <a-avatar id="avatar" shape="square" :size="128" icon="user" />
      <h1 id="username">USERNAME</h1>
      <p id="sign">Lorem ipsum dolor sit amet, consectetur adipisicing elit</p>
      <a-button id="infochange" @click="emitClick">修改个人简介</a-button>
    </div>
</template>

<script>
    export default {
        name: "personInfo.vue",
      methods: {
          emitClick: function () {
            console.log('Change info button clicked')
            this.$emit('clickInfoChange')
          }
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
    background-image: url("../assets/info.jpg");
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
  }
  #avatar {
    position: absolute;
    bottom: 15px;
    left: 15px;

  }
  #username {
    margin: 0 auto 0 180px;
    font-size: 35px;
  }
  #sign {
    margin: 0 auto 0 180px;
  }
  #infochange {
    position: absolute;
    right: 0;
    bottom: 0;
    margin-right: 10px;
    margin-bottom: 10px;
  }
</style>
