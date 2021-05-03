<template>
  <div class="hello" id="hello">
    <div id="logo">
      <img src="../assets/custom_logo_1.png">
    </div>
    <h1>{{ msg }}</h1>
    <ul id="links">
      <li>
        <a
          href="malls">
<!--          target="_blank"-->
          Malls
        </a>
      </li>
      <li>
        <a
          href="shops">
<!--          target="_blank"-->
<!--        >-->
          Shops
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to ShopFinder'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
  margin: 50px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#hello {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}
#links {
  font-size: 2rem;
}
</style>
