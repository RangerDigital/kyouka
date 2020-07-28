<template>
<button class="button button-flex g-clickable" @click="$emit('clickEvent');">
  <slot>CLICK ME</slot>
</button>
</template>

<script>
export default {
  name: 'SmallButton',
}
</script>

<style scoped>
.button {
  width: 6rem;
  height: 6rem;
  margin: 0 auto;
  background-color: #3D3D3D;
  border: none;
  border-radius: 4px;
  margin: 1em;

  box-shadow: inset 31px 31px 62px #343434, 
            inset -31px -31px 62px #464646;
}

.button-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}

.button img {
  height: 2rem;
  width: 2rem;
  margin: 0.6em;
}

.button:active {
  transform: translateY(4px);
  transform: scale(0.95);
}
</style>