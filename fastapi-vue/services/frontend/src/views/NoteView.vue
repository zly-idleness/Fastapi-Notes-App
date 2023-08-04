<template>
    <div class="note-view">
        <div class="note-details">
            <div v-if="note">
                <p class="note-detail"><strong>Title:</strong> {{ note.title }}</p>
                <p class="note-detail"><strong>Content:</strong> {{ note.content }}</p>
                <p class="note-detail"><strong>Author:</strong> {{ note.author.username }}</p>

                <div v-if="user.id === note.author.id" class="note-actions">
                    <router-link :to="{ name: 'EditNote', params: { id: note.id } }" class="btn btn-primary">
                        Edit
                    </router-link>
                    <button @click="removeNote()" class="btn btn-secondary">
                        Delete
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
  

  
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Note',
    props: ['id'],
    async created() {
        try {
            await this.viewNote(this.id);
        } catch (error) {
            console.error(error);
            this.$router.push('/dashboard');
        }
    },
    computed: {
        ...mapGetters({ note: 'stateNote', user: 'stateUser' }),
    },
    methods: {
        ...mapActions(['viewNote', 'deleteNote']),
        async removeNote() {
            try {
                await this.deleteNote(this.id);
                this.$router.push('/dashboard');
            } catch (error) {
                console.error(error);
            }
        }
    },
});
</script>
  
<style scoped>
.note-view {
    margin-top: 100px;
    /* Add more space from the NavBar */
}

.note-details {
    margin-top: 20px;
    /* Add space between items */
}

.note-detail {
    margin-bottom: 10px;
    /* Add space below each item */
}

.note-actions {
    margin-top: 20px;
    /* Add space above action buttons */
}
</style>


  