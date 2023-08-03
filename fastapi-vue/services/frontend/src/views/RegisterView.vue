<template>
    <section class="register-view">
        <form @submit.prevent="submit" class="register-form">
            <div class="mb-3">
                <label for="username" class="form-label">Username:</label>
                <input type="text" name="username" v-model="user.username" class="form-control" />
            </div>
            <div class="mb-3">
                <label for="full_name" class="form-label">Full Name:</label>
                <input type="text" name="full_name" v-model="user.full_name" class="form-control" />
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" name="password" v-model="user.password" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </section>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
    name: 'Register',
    data() {
        return {
            user: {
                username: '',
                full_name: '',
                password: '',
            },
        };
    },
    methods: {
        ...mapActions(['register']),
        async submit() {
            try {
                await this.register(this.user);
                this.$router.push('/dashboard');
            } catch (error) {
                throw 'Username already exists. Please try again.';
            }
        },
    },
});
</script>
  
<style scoped>
.register-form {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: white;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.form-label {
    font-weight: bold;
}


.form-control {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}
</style>
  
<style scoped>
.register-view {
    margin-top: 20px;
    /* Adjust the margin as needed */
    padding: 20px;
    /* Add padding as needed */
}
</style>