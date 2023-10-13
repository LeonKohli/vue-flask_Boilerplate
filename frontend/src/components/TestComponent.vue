<template>
    <div class="bg-green-500 text-white p-4 rounded">
      {{ message }}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "TestComponent",
    data() {
        return {
            message: 'Fetching...'
        };
    },
    created() {
        axios.get('http://localhost:5000/api/test')
            .then(response => {
                this.message = response.data.message;
            })
            .catch(error => {
                this.message = `Error fetching data: ${error.message}`;
            });
    }
};
</script>
