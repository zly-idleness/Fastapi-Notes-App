<template>
    <div class="note-view">
        <div class="note-details">
            <div v-if="note">
                <div class="note-summary">
                    <p class="note-detail"><strong>Title:</strong> {{ note.title }}</p>
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

                <div class="note-content-card">
                    <div class="card">
                        <div class="card-body">
                            <p class="note-content">{{ note.content }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Note-layout',
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
    /* Add space between details and actions */
}

.note-detail {
    margin-bottom: 10px;
    /* Add space below each detail */
}

.note-actions {
    margin-top: 20px;
    /* Add space above action buttons */
}
</style>






<style scoped>
.note-content-card {
    margin-top: 20px;
}

.card {
    background-color: #F7F7F7;
    border: 1px solid #CCC;
    border-radius: 10px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.card-body {
    padding: 20px;
}

.note-content {
    font-size: 16px;
    line-height: 1.6;
}
</style>
  
  