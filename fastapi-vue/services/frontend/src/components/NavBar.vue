<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-light bg-light bg-blue">
            <div class="container d-flex justify-content-between">
                <img src="@/assets/logo-b.png" alt="Logo" class="navbar-logo">
                <router-link class="navbar-brand" to="/">My APP</router-link>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav d-flex me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <router-link class="nav-link" to="/">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/profile">My Profile</router-link>
                        </li>
                        <li class="nav-item" v-if="isLoggedIn">
                            <a class="nav-link" @click="logout">Log Out</a>
                        </li>
                        <template v-else>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/register">Register</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/login">Log In</router-link>
                            </li>
                        </template>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
</template>
  
<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'NavBar',
    computed: {
        isLoggedIn: function () {
            return this.$store.getters.isAuthenticated;
        },
    },
    methods: {
        async logout() {
            await this.$store.dispatch('logOut');
            this.$router.push('/login');
        },
    },
});
</script>
  
<style scoped>
a {
    cursor: pointer;
    color: #333;
}

.navbar {
    background-color: #5bd4af;
    padding: 15px 0;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-logo {
    height: 60px;
    margin-right: 50px;
}

.navbar-toggler-icon {
    background-color: #333;
}

.nav-link {
    color: #555;
    /* Adjusted text color for better readability */
    transition: color 0.3s;
}

.navbar-nav .nav-link {
    font-size: 20px;
}

.nav-link:hover {
    color: #f39c12;
}

.bg-blue {
    background-color: #3498db;
    /* Adjust the shade of blue as needed */
}

/* Styling for guest navigation items */
.guest-nav .nav-link {
    color: #5ea7ec;
}
</style>
  