// global vars
var note_count = 0
var c_index = 0

document.getElementById("add_note").addEventListener("click", function(){
    /*
    Basic click listener:
    1. if text is empty, return an error.
    2. else create a new template div and add it to our "existing notes"
    */
    var text = document.getElementById("new_note");
    var newmessage = text.value
    if (newmessage.length <= 0){
       return window.alert("No note added!");
    }
    note_count += 1 // inc note count now we know its valid.
    var made_div = document.getElementById("existing_notes");
    
    if (note_count == 1) {
        // if this is the first new note, we need to display
        // the list of our existing notes.
        to_hide = document.getElementById("notes_info");
        to_hide.style.display = 'inline';
    }
    var new_div = get_new_div()
    // create new textarea & delete button
    var new_note = create_new_textarea(newmessage);
    var delbutton = get_delete_button();
    /// add note & button to div
    new_div.appendChild(new_note);
    new_div.appendChild(delbutton);
    // add our new note to the existing div
    made_div.insertBefore(new_div, made_div.children[0]);
    // remove passed in text
    text.value = "";
});


function create_new_textarea(newmessage) {
    /* 
     Create new textare, set rows to 4 and insert new message
    */
    var new_note = document.createElement("textarea");
    new_note.readonly = 'true';
    new_note.rows = '4'
    new_note.value = newmessage;
    new_note.className = 'inserted_node';
    return new_note
};


function get_new_div() {
    /* 
    Return a new div for a new note
    */
    var new_div = document.createElement("div");
    new_div.style.backgroundColor = pick_colour()
    new_div.className = "noteDiv"
    return new_div
};


function get_delete_button(){
    /*
    Create & return a new delete button:
    define an onclick func to remove the node and decrement the count of active notes
    */

    var delbutton = document.createElement("button");
    var button_text = document.createTextNode("Delete");
    delbutton.onclick = function(){
        // func to remove this node from parent node when clicked.
        var notes = document.getElementById("existing_notes")
        notes.removeChild(this.parentNode);
        note_count -= 1;
        if (note_count == 0){
            // hide yoke.
            to_hide = document.getElementById("notes_info");
            to_hide.style.display = 'none';
        }
        return true
    };
    delbutton.className = "delete_button";
    delbutton.appendChild(button_text);
    return delbutton
}


function pick_colour() {
    /*
    Return the next colour based on a global
    index - allows for always alternating colours
    (until a user deletes one)
    */
    var colours = ["#88a3ad", "#aab9bd", "#cccaca", "#f0eceb", "#f0e4dd"];
    // picked them from https://www.color-hex.com/color-palette/77356
    new_colour = colours[c_index];
    if (c_index < (colours.length - 1)){
        c_index += 1;
    }
    else{
        c_index = 0;
    }
    return new_colour;
};

