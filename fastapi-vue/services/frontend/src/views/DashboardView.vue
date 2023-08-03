<template>
    <div class="dashboard">
        <section class="add-note-section">
            <h1>Add New Note</h1>
            <hr />
            <form @submit.prevent="submit" class="note-form">
                <div class="form-group">
                    <label for="title" class="form-label">Title:</label>
                    <input type="text" name="title" v-model="form.title" class="form-control" />
                </div>
                <div class="form-group">
                    <label for="content" class="form-label">Content:</label>
                    <textarea name="content" v-model="form.content" class="form-control"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </section>

        <section class="notes-section">
            <h1>Notes</h1>
            <hr />
            <div v-if="notes.length">
                <div v-for="note in notes" :key="note.id" class="note-card">
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                            <ul>
                                <li><strong>Note Title:</strong> {{ note.title }}</li>
                                <li><strong>Author:</strong> {{ note.author.username }}</li>
                                <li><router-link :to="{ name: 'Note', params: { id: note.id } }">View</router-link></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <p>Nothing to see. Check back later.</p>
            </div>
        </section>
    </div>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Dashboard',
    data() {
        return {
            form: {
                title: '',
                content: '',
            },
        };
    },
    created() {
        this.$store.dispatch('getNotes');
    },
    computed: {
        ...mapGetters({ notes: 'stateNotes' }),
    },
    methods: {
        ...mapActions(['createNote']),
        async submit() {
            await this.createNote(this.form);
        },
    },
});
</script>
  
<style scoped>
.dashboard {
    padding: 20px;
}

.add-note-section,
.notes-section {
    margin-bottom: 40px;
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

.note-card {
    margin-bottom: 20px;
}
</style>
  