<template>
    <section class="edit-note-section">
        <h1>Edit Note</h1>
        <hr /><br />

        <form @submit.prevent="submit" class="edit-note-form">
            <div class="mb-3">
                <label for="title" class="form-label">Title:</label>
                <input type="text" name="title" v-model="form.title" class="form-control" />
            </div>
            <div class="mb-3">
                <label for="content" class="form-label">Content:</label>
                <div class="editor-container">
                    <md-editor v-model="form.content" />
                </div>
            </div>
            <div class="mb-4">
                <button type="submit" class="btn btn-primary">Submit</button>
            </div>
        </form>
    </section>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';

export default defineComponent({
    name: 'EditNote',
    components: { MdEditor },
    props: ['id'],
    data() {
        return {
            form: {
                title: '',
                content: '',
            },
        };
    },
    created: function () {
        this.GetNote();
    },
    computed: {
        ...mapGetters({ note: 'stateNote' }),
    },
    methods: {
        ...mapActions(['updateNote', 'viewNote']),
        async submit() {
            try {
                let note = {
                    id: this.id,
                    form: this.form,
                };
                await this.updateNote(note);
                this.$router.push({ name: 'Note', params: { id: this.note.id } });
            } catch (error) {
                console.log(error);
            }
        },
        async GetNote() {
            try {
                await this.viewNote(this.id);
                this.form.title = this.note.title;
                this.form.content = this.note.content;
            } catch (error) {
                console.error(error);
                this.$router.push('/dashboard');
            }
        },
    },
});
</script>
<style scoped>
.edit-note-section {
    margin-top: 40px;
    /* Add space from the NavBar */
}

.edit-note-form {
    margin-top: 20px;
    /* Add space between form sections */
}

.md-editor-container {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
}

.md-editor-toolbar {
    background-color: #f5f5f5;
    border-radius: 5px 5px 0 0;
    padding: 5px 10px;
}

.md-editor-content {
    border-top: 1px solid #ccc;
    padding: 10px;
}

.md-editor-preview {
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 0 0 5px 5px;
}

.edit-note-content {
    height: 200px;
    /* Adjust textarea height as needed */
}
</style>
