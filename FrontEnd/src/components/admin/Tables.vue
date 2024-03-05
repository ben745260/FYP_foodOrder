<template>
    <div>
        <h1>Tables</h1>
        <!-- Your tables content here -->
        <button @click="goToMenu">Go to Menu</button>

    </div>
</template>
  
<script>
export default {
    name: 'Tables',
    // Add any additional logic or data properties here
    methods: {
        goToMenu() {
            this.$router.push('/table/tabelmenu');
        }
    }
};
</script>