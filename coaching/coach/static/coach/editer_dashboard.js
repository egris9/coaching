
window.onload = function(){
    const Header=window.Header
    const List=window.List
const editor = new EditorJS({
    tools: {
        header: {
          class: Header,
          shortcut: 'CMD+SHIFT+H',
        },
        list: {
          class: List,
          inlineToolbar: true,
          config: {
            defaultStyle: 'unordered'
          }
        },
      },
    holder:"editorjs"
});
};