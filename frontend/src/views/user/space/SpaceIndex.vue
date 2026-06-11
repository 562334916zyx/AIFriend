<script setup>
import {useRoute} from "vue-router";

const router = useRoute();
</script>

<template>
个人空间: {{ router.params.user_id}}
</template>

<style scoped>

</style>