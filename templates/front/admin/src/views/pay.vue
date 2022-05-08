<template>
  <div class="container">
    <el-alert title="Please check the order information before confirming payment" type="success" :closable="false"></el-alert>
    <!-- <div class="top-content">
      <span>payee</span>
      <el-input style="width:300px" v-model="name" placeholder="payee"></el-input>
      <span style="margin-left:20px">shroff account number</span>
      <el-input style="width:300px" v-model="account" placeholder="shroff account number"></el-input>
    </div> -->
    <!-- <div class="price-content">
      <span>money</span>
      <span>￥99.0</span>
    </div> -->
    <div class="pay-type-content">
      <div class="pay-type-item">
        <el-radio v-model="type" label="WeChat Pay"></el-radio>
        <img src="@/assets/img/test/weixin.png" alt>
        <!-- <span>WeChat Pay</span> -->
      </div>
      <div class="pay-type-item">
        <el-radio v-model="type" label="use Alipay to pay"></el-radio>
        <img src="@/assets/img/test/zhifubao.png" alt>
        <!-- <span>use Alipay to pay</span> -->
      </div>
      <div class="pay-type-item">
        <el-radio v-model="type" label="CCB"></el-radio>
        <img src="@/assets/img/test/jianshe.png" alt>
        <!-- <span>CCB</span> -->
      </div>
      <div class="pay-type-item">
        <el-radio v-model="type" label="The Agricultural Bank of China"></el-radio>
        <img src="@/assets/img/test/nongye.png" alt>
        <!-- <span>The Agricultural Bank of China</span> -->
      </div>
      <div class="pay-type-item">
        <el-radio v-model="type" label="Chinese bank"></el-radio>
        <img src="@/assets/img/test/zhongguo.png" alt>
        <!-- <span>Chinese bank</span> -->
      </div>
      <div class="pay-type-item">
        <el-radio v-model="type" label="Bank of Communications"></el-radio>
        <img src="@/assets/img/test/jiaotong.png" alt>
        <!-- <span>Bank of Communications</span> -->
      </div>
    </div>
    <div class="buton-content">
      <el-button @click="submitTap" type="primary">pay</el-button>
      <el-button @click="back()">back</el-button>
    </div>
  </div>
</template>
<script>
// import { Message } from "element-ui";
export default {
  data() {
    return {
      name: "",
      account: "",
      type: "",
      table: "",
      obj: ""
    };
  },
  mounted() {
    let table = this.$storage.get("paytable");
    let obj = this.$storage.getObj("payObject");
    this.table = table;
    this.obj = obj;
  },
  methods: {
    submitTap() {
      // if (!this.name) {
      //   this.$message.error("Please input payee name");
      //   return;
      // }
      // if (!this.account) {
      //   this.$message.error("Please enter the payee account number");
      //   return;
      // }
      if (!this.type) {
        this.$message.error("Please select payment method");
        return;
      }
      this.$confirm(`pay?`, "reminder", {
        confirmButtonText: "yes",
        cancelButtonText: "cancel",
        type: "warning"
      }).then(() => {
        this.obj.ispay = "paid";
        this.$http({
          url: `${this.table}/update`,
          method: "post",
          data: this.obj
        }).then(({ data }) => {
          if (data && data.code === 0) {
            this.$message({
              message: "payment success",
              type: "success",
              duration: 1500,
              onClose: () => {
                this.$router.go(-1);
              }
            });
          } else {
            this.$message.error(data.msg);
          }
        });
      });
    },
    back(){
      this.$router.go(-1);
    }
  }
};
</script>
<style lang="scss" scoped>
.container {
  margin: 10px;
  font-size: 14px;
  span {
    width: 60px;
  }
  .top-content {
    display: flex;
    align-items: center;
    padding: 20px;
  }
  .price-content {
    display: flex;
    align-items: center;
    margin-top: 20px;
    padding-bottom: 20px;
    padding: 20px;
    border-bottom: 1px solid #eeeeee;
    font-size: 20px;
    font-weight: bold;
    color: red;
  }
  .pay-type-content {
    display: flex;
    align-items: center;
    margin-top: 20px;
    flex-wrap: wrap;
    span {
      width: 100px;
    }
    .pay-type-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 300px;
      margin: 20px;
      border: 1px solid #eeeeee;
      padding: 20px;
    }
  }
  .buton-content {
    margin: 20px;
  }
}
</style>
