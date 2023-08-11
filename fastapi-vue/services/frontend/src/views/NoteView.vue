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
                <div>
                    <MdPreview class="left-aligned-editor" previewTheme=vuepress :editorId="id"
                        :modelValue="note.content" />
                </div>

            </div>
        </div>
    </div>
</template>
  

<script setup>
import { MdPreview } from 'md-editor-v3';
import 'md-editor-v3/lib/preview.css';

const id = 'preview';

</script>

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
    padding: 20px;
    margin-top: 40px;
    /* Add more space from the NavBar */
}

.note-summary {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 20px;
    font-size: 22px;
    font-weight: bold;
    /* Add space below summary */
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
    padding: 20px;
    margin-top: 20px;
    /* Add space above action buttons */
}

.left-aligned-editor {
    background-color: rgb(170, 223, 199);
    padding: 20px;
    text-align: left;
}
</style>
  
  