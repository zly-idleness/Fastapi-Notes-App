<template>
    <section class="profile-view">
        <h1>Your Profile</h1>
        <hr /><br />
        <div class="profile-info">
            <p><strong>Full Name:</strong> <span>{{ user.full_name }}</span></p>
            <p><strong>Username:</strong> <span>{{ user.username }}</span></p>
            <p>
                <button @click="deleteAccount()" class="btn btn-danger">Delete Account</button>
            </p>
        </div>
    </section>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Profile-layout',
    created: function () {
        return this.$store.dispatch('viewMe');
    },
    computed: {
        ...mapGetters({ user: 'stateUser' }),
    },
    methods: {
        ...mapActions(['deleteUser']),
        async deleteAccount() {
            try {
                await this.deleteUser(this.user.id);
                await this.$store.dispatch('logOut');
                this.$router.push('/');
            } catch (error) {
                console.error(error);
            }
        },
    },
});
</script>
  
<style scoped>
.profile-view {
    padding: 20px;
}

.profile-info {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: white;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.btn-danger {
    background-color: #dc3545;
    border-color: #dc3545;
    color: white;
}

.btn-danger:hover {
    background-color: #c82333;
    border-color: #bd2130;
    color: white;
}
</style>
  