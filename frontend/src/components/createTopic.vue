<template>
  <div class="outerbody">
    <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol" :rules="rules" ref="ruleForm">
      <a-form-model-item ref="name" prop="name" label="标题">
        <a-input v-model="form.name" placeholder="请输入标题"
                 @blur="
                    () => {
                      $refs.name.onFieldBlur();
                    }
                  "/>
      </a-form-model-item>
      <a-form-model-item label="正文">
        <a-input v-model="form.desc" type="textarea"  :auto-size="{ minRows: 4, maxRows: 8 }"/>
      </a-form-model-item>
      <a-form-model-item label="到期自动删除主题">
        <a-switch v-model="form.expire" @change="expireChange"/>
      </a-form-model-item>
      <a-form-model-item label="主题可见至" v-if="isExpire===true">
        <a-date-picker
          v-model="form.date"
          show-time
          type="date"
          placeholder="请选择日期时间"
          style="width: 100%;"
        />
      </a-form-model-item>
      <a-form-model-item label="匿名发布">
        <a-switch v-model="form.anonymous" />
      </a-form-model-item>
      <a-form-model-item label="上传图片（最多九张）">
        <div class="clearfix">
          <a-upload
            action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
            list-type="picture-card"
            :file-list="fileList"
            @preview="handlePreview"
            @change="handleChange"
          >
            <div v-if="fileList.length < 9">
              <a-icon type="plus" />
              <div class="ant-upload-text">
                上传图片
              </div>
            </div>
          </a-upload>
          <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel">
            <img alt="example" style="width: 100%" :src="previewImage" />
          </a-modal>
        </div>
      </a-form-model-item>
      <a-form-model-item :wrapper-col="{ span: 14, offset: 6 }">
        <a-button type="primary" @click="onSubmit">
          确认发布
        </a-button>
        <a-button style="margin-left: 10px;" @click="onThrow">
          取消发布
        </a-button>
      </a-form-model-item>
    </a-form-model>
  </div>
</template>

<script>
  function getBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = error => reject(error);
    });
  }
  export default {
    name: "createTopic.vue",
    data() {
      return {
        labelCol: { span: 6 },
        wrapperCol: { span: 14 },
        form: {
          name: '',
          desc: '',
          date: undefined,
          expire: false,
          anonymous: false,
        },
        previewVisible: false,
        previewImage: '',
        fileList: [],
        isExpire: false,
        rules: {name:[{ required: true, message: '标题不能为空', trigger: 'blur' }]}
      };
    },
    methods: {
      onSubmit() {
        this.$refs.ruleForm.validate(valid => {
          if(valid) {
            console.log('submit!', this.form);
            console.log(this.fileList);
            this.$emit('submitTopic');
          } else {
            console.log('Invalid submit!');
            return false;
          }
        })
      },
      onThrow() {
        console.log('This topic was thrown')
        this.$emit('throwTopic');
      },
      handleCancel() {
        this.previewVisible = false;
      },
      async handlePreview(file) {
        if (!file.url && !file.preview) {
          file.preview = await getBase64(file.originFileObj);
        }
        this.previewImage = file.url || file.preview;
        this.previewVisible = true;
      },
      handleChange({ fileList }) {
        this.fileList = fileList;
      },
      expireChange(changed) {
        if (changed === true) {
          this.isExpire = true;
        } else {
          this.isExpire = false;
        }
      }
    },
  }
</script>

<style scoped>
.outerbody {
  width: 67%;
  margin: 15px auto;
}
.ant-upload-select-picture-card i {
  font-size: 32px;
  color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
</style>
