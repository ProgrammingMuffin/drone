<template>
<button class="wide_button" @click="init_gpio" >Init GPIO</button>
<br/><br/><br/>
<button class="wide_button" @click="clear_gpio" >Clear GPIO</button>
<br/><br/><br/>
<input type="number" class="input" v-model="duty" />
<button class="action_button" @click="change_duty_cycle" >Go</button>
<br/><br/><br/>
responses:
<br/><br/>
<div>{{ response }}</div>
</template>


<script>
  export default {
      data () {
	  return {
	      response: "",
	      host: "192.168.0.103"
	  };
      },
      methods: {
	  init_gpio() {
	      fetch("http://" + this.host + ":5002/gpio", {method: "POST"})
		  .then((res) => { this.response = res.toString() })
		  .catch((err) => { this.response = err.toString() });
	  },
	  clear_gpio() {
	      fetch("http://" + this.host + ":5002/gpio", {method: "DELETE"})
		  .then((res) => { this.response = res.toString() })
		  .catch((err) => { this.response = err.toString() });
	  },
	  change_duty_cycle() {
	      fetch("http://" + this.host + ":5002/duty/" + this.duty, {method: "PATCH"})
		  .then((res) => { this.response = res.toString() })
		  .catch((err) => { this.response = err.toString() });
	  }
      }
  }
</script>
