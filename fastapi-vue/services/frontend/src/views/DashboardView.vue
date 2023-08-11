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
                    <div class="mb-3">
                        <MdEditor class="left-aligned-editor" previewTheme=vuepress v-model="form.content" />
                    </div>
                </div>
                <div class="form-group" style="margin-top: 20px;">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </section>

        <section class="notes-section">
            <h1>Notes</h1>
            <hr />
            <div v-if="notes && notes.length" class="notes-grid">
                <div v-for="note in notes" :key="note.id" class="note-card">
                    <div class="card">
                        <div class="card-body">
                            <div class="note-content">
                                <h2 class="note-title">{{ note.title }}</h2>

                            </div>
                            <div class="note-details">
                                <ul>
                                    <li><strong>Author:</strong> {{ note.author.username }}</li>
                                    <li><router-link :to="{ name: 'Note', params: { id: note.id } }">View</router-link></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <p>No notes available. Check back later.</p>
            </div>
        </section>
    </div>
</template>
  

<script setup>
import { MdEditor } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';

</script>

  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Dashboard-layout',
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
        truncateContent(content) {
            if (content.length > 40) {
                return content.substring(0, 40) + ' ...';
            }
            return content;
        },
    },
});
</script>
  
<style scoped>
.dashboard {
    padding: 20px;
}

.form-control {
    width: 100%;
    font-weight: bold;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

.notes-section {
    margin-bottom: 20px;
}

.note-content-preview {
    font-size: 14px;
    margin-top: 10px;
    color: #888;
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
    background-color: #9bc9bf;
    border-color: #64b8b4;
    font-size: 16px;
    /* Increase button font size */
    padding: 10px 20px;
    /* Add padding to the button */
}

.btn-primary:hover {
    background-color: #4fa68f;
    border-color: #4098a2;
}


.note-title {
    font-size: 18px;
    /* Increase title font size */
    font-weight: bold;
    margin-bottom: 5px;
}

.note-content {
    font-size: 18px;
    font-weight: bold;
    /* Increase content font size */
}

.notes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(18rem, 1fr));
    grid-gap: 10px;
}

.note-card {
    margin-bottom: 20px;
    background-color: #F3F3F3;
    /* Light gray background for note cards */
    border: 1px solid #DDD;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.left-aligned-editor {
    background-color: rgb(232, 246, 240);
    padding: 20px;
    text-align: left;
}

.card {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
</style>
  