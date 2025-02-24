<template>
  <div id="app" class="g-full-page">
    <section class="header">
      <h1>Kyouka</h1>
      <p>Server: {{ getServer }}</p>
      <p class="error">{{ errorMsg }}</p>
    </section>

    <div class="buttons-container">
      <BigButton @clickEvent="sendAction('/track/previous')" aria-label="Previous Track"><img src="./assets/previous.svg"/></BigButton>
      <BigButton @clickEvent="sendAction('/track/play')" class="red-bg" aria-label="Pause/Play Track"><img src="./assets/play.svg"/></BigButton>
      <BigButton @clickEvent="sendAction('/track/next')" aria-label="Next Track"><img src="./assets/next.svg"/></BigButton>
    </div>

    <section>
      <p>Volume Control</p>
      <div class="divider"></div>
      <div class="buttons-container">
        <SmallButton @clickEvent="sendAction('/volume/up')" aria-label="Volume Up"><img src="./assets/up.svg"/></SmallButton>
        <SmallButton @clickEvent="sendAction('/volume/mute')" aria-label="Mute"><img src="./assets/mute.svg"/></SmallButton>
        <SmallButton @clickEvent="sendAction('/volume/down')" aria-label="Volume Down"><img src="./assets/down.svg"/></SmallButton>
      </div>
    </section>

    <FooterBar />
  </div>
</template>

<script>
  import SmallButton from "./components/SmallButton.vue";
  import BigButton from "./components/BigButton.vue";
  import FooterBar from "./components/FooterBar.vue";

  export default {
    name: "App",
    components: {
      BigButton,
      FooterBar,
      SmallButton,
    },
    data() {
      return {
        errorMsg: "",
      };
    },
    methods: {
      sendAction(action) {
        window.navigator.vibrate(50);

        this.$http
          .post("http://" + location.host + action, { timeout: 500 })
          .then((response) => {
            console.log(response);
            this.errorMsg = "";
          })
          .catch((error) => {
            console.log(error.response.data.msg);
            this.errorMsg = "Something went wrong while connecting to the server!";
            window.navigator.vibrate([50, 50, 50, 50, 50]);
          });
      },
    },
    computed: {
      getServer: function() {
        return location.host;
      },
    },
  };
</script>

<style>
  @import "./assets/css/reset.css";
  @import url("https://fonts.googleapis.com/css?family=Baloo+Thambi+2&display=swap");

  html {
    font-size: 10px;
    background-color: #efe7e7;
  }

  h1 {
    font-size: 2.7rem;
    font-weight: 600;
    font-family: "Baloo Thambi 2";
    color: #3d3d3d;
    letter-spacing: 0.05em;
    margin-bottom: 0.25em;
  }

  p {
    font-size: 1.6rem;
    font-weight: 500;
    font-family: "Baloo Thambi 2";
    color: #aaa5a5;
    letter-spacing: 0.05em;
    text-align: center;
  }

  .g-full-page {
    padding: 2rem;
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }

  .g-clickable {
    cursor: pointer;
    outline: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }

  .buttons-container {
    display: flex;
    align-items: center;
    justify-content: space-around;
  }

  .red-bg {
    background-color: #ff7171 !important;
  }

  .divider {
    margin: 0 auto;
    height: 1.5px;
    width: 100%;
    background-color: #aaa5a5;
    border-radius: 100px;

    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  .header {
    align-self: flex-start;
    text-align: left;
  }

  .header p {
    text-align: left;
  }

  .error {
    color: #ff7171;
  }

  @media only screen and (min-width: 1500px) {
    html {
      font-size: 11px;
    }

    .g-full-page {
      padding: 3rem;
    }
  }

  @media only screen and (min-width: 2000px) {
    html {
      font-size: 15px;
    }

    .g-full-page {
      padding: 5rem;
    }
  }

  @media only screen and (max-height: 500px) {
    .g-full-page {
      height: 150vh;
    }
  }
</style>
