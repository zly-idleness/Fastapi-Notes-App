<template>
    <form @submit.prevent="submit" class="edit-note-form">
        <div class="mb-3">
            <label for="title" class="form-label">Title:</label>
            <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
            <MdEditor class="left-aligned-editor" previewTheme=smart-blue v-model="form.content" :sanitize="sanitize" />
        </div>
        <div class="mb-4">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>
</template>
  
<script setup>
import sanitizeHtml from 'sanitize-html';
import { MdEditor } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';

const sanitize = (html) => {
    return sanitizeHtml(html);
};
</script>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';


export default defineComponent({
    name: 'EditNote-layout',
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
.left-aligned-editor {
    text-align: left;
}
</style>
