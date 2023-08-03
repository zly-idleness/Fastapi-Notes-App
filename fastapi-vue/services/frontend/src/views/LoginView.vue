<template>
    <section class="login-view">
        <form @submit.prevent="submit" class="login-form">
            <div class="form-group">
                <label for="username" class="form-label">Username:</label>
                <input type="text" name="username" v-model="form.username" class="form-control" />
            </div>
            <div class="form-group">
                <label for="password" class="form-label">Password:</label>
                <input type="password" name="password" v-model="form.password" class="form-control" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </section>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
    name: 'Login',
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
        };
    },
    methods: {
        ...mapActions(['logIn']),
        async submit() {
            const userFormData = new FormData();
            userFormData.append('username', this.form.username);
            userFormData.append('password', this.form.password);
            await this.logIn(userFormData);
            this.$router.push('/dashboard');
        },
    },
});
</script>
  
<style scoped>
.login-view {
    margin-top: 20px;
    /* Add space between NavBar and LoginView */
    display: flex;
    justify-content: center;
    align-items: center;
    height: calc(80vh - 20px);
    /* Adjust to your Navbar height */
}

.login-form {
    width: 100%;
    max-width: 400px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: white;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-label {
    font-weight: bold;
}

.form-control {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

.btn-primary {
    width: 100%;
}
</style>
  