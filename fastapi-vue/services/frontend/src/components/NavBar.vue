<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark bg-dark">
            <div class="container d-flex justify-content-between">
                <img src="@/assets/logo.png" alt="Logo" class="navbar-logo">
                <a class="navbar-brand" href="/"> My APP</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul v-if="isLoggedIn" class="navbar-nav d-flex me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <router-link class="nav-link" to="/">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/profile">My Profile</router-link>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" @click="logout">Log Out</a>
                        </li>
                    </ul>
                    <ul v-else class="navbar-nav d-flex me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <router-link class="nav-link" to="/">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/register">Register</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/login">Log In</router-link>
                        </li>
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
        }
    },
    methods: {
        async logout() {
            await this.$store.dispatch('logOut');
            this.$router.push('/login');
        }
    },
});
</script>
  
<style scoped>
a {
    cursor: pointer;
    color: white;
}

.navbar {
    background-color: #343a40;
}

.navbar-logo {
    height: 100px;
    /* Adjust the height as needed */
    margin-right: 50px;
    /* Adjust the margin as needed */
}



.navbar-toggler-icon {
    background-color: white;
}

.nav-link {
    color: white;
    transition: color 0.3s;
}

.navbar-nav .nav-link {
    font-size: 20px;
    /* Adjust the font size as needed */
}

.nav-link:hover {
    color: #f39c12;
}
</style>
  