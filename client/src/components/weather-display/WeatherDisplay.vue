<script lang="ts">
import { defineComponent } from "vue";
import WeatherDisplayMini from "../weather-display-mini/WeatherDisplayMini.vue";

export default defineComponent({
  name: "WeatherDisplay",
  components: { WeatherDisplayMini },
});
</script>

<template>
  <div class="main-view">
    <div class="left-view">
      <div class="header">
        <h2>Toronto</h2>
        <h3>21.03.2021</h3>
      </div>
      <div class="content">
        <div class="temp">
          <span class="degrees">14&deg;</span>
          <span class="desc">Cloudy</span>
        </div>
        <div class="daily">
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
        </div>
      </div>
    </div>

    <div class="right-view">
      <div class="header">
        <h3>Good Morning</h3>
        <h3>10:30</h3>
      </div>

      <div class="content">
        <div class="temp">
          <span class="degrees">14&deg;</span>
          <span class="feel">Feels like 19&deg;</span>
          <span class="desc">Cloudy</span>
          <span class="daily-desc">Hourly Forecast</span>
        </div>
        <div class="hourly">
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
          <WeatherDisplayMini></WeatherDisplayMini>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-view {
  display: flex;
}

.left-view {
  flex-grow: 1;

  .header {
    display: flex;

    h3 {
      margin-left: 555px;
      flex-grow: 1;
    }

    h2 {
      margin-left: 85px;
      flex-grow: 1;
    }
  }

  .content {
    text-align: center;

    .temp {
      display: flex;
      flex-direction: column;

      .degrees {
        font-size: 20vmin;
      }

      .feel {
        font-size: 1vmin;
      }

      .desc {
        font-size: 4vmin;
      }
    }

    .daily {
      display: flex;
      justify-content: space-evenly;
    }
  }
}

.right-view {
  padding-left: 50px;
  text-align: center;
  background-color: #f6f6f6;
  width: 20%;

  .header {
    margin-top: 10px;
  }

  .temp {
    display: flex;
    flex-direction: column;

    .degrees {
      font-size: 3vmin;
    }

    .feel {
      font-size: 1.8vmin;
    }

    .desc {
      font-size: 2.5vmin;
    }

    .daily-desc {
      font-size: 2vmin;
    }
  }
  .hourly {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }
}
</style>
