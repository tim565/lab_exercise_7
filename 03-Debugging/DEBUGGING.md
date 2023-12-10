<h1>DEBUGGING</h1>

# RUN OPERATIONS

| Operation                           | MacOS Shortcut | Windows / Linux Shortcut |
|-------------------------------------|----------------|--------------------------|
| Run current file in console         | ^ Enter        |                          |
| Execute selection in Python console | ⌥⇧E            |                          |
| Run current file                    | ^⇧ R           |                          |
| Re-run last configuration           | ^ R            |                          |

# DEBUG OPERATIONS

| Operation                        | MacOS Shortcut | Windows / Linux Shortcut |
|----------------------------------|----------------|--------------------------|
| Debug current file               | ^⇧ D           |                          |
| Restart last debug configuration | ^ D            |                          |

## Debug Pane

| Important Operations | 
|----------------------|
| Resume program       |
| Step over            |
| Step into            |
| Step out             |

<div class="exercise box">

###### 🧑‍💻 Lab Exercise: Debugging

Please go to the '**guess_the_number.py**' within the same directory with this
document and follow the instructions in it. All exercise instructions in .py
files are marked with a '🧑‍TODO' indicator).

</div>




<h1>Appendix</h1>

[Notebook Style]

<style>

    :root {
        --lineHeight: 20px;
        --max-width: 510px;
    }

    img {
        border-radius: 6px;
    }

    /* ----- VARIOUS BOXES -------------------------------------------------- */


    .box {
        margin-top: 15px;
        padding: 5px 20px 5px 20px;
        border-width: 1.5px;
        border-style: solid;
        border-radius: 6px;
        line-height: var(--lineHeight);
        max-width: var(--max-width);
    }

    /* Placeholders are for instructions such as `Enter your answer here' */
    .placeholder, .answer-container {  /* gray, dashed*/
        max-width: var(--max-width);
        color: rgb(130, 130, 130);
        padding: 16px 10px;
        border: 1px dashed rgb(130, 130, 130);
        border-radius: 6px;
        font-family: "Courier New", Courier, monospace;
        line-height: var(--lineHeight);
    }

    /* Code placeholders are pre-filled */
    .placeholder-code {  /* gray, dashed*/
        max-width: var(--max-width);
        color: rgb(130, 130, 130);
        padding: 16px 10px;
        border: 1px dashed rgb(130, 130, 130);
        border-radius: 6px;
        font-family: "Courier New", Courier, monospace;
        line-height: var(--lineHeight);
    }
    .placeholder-code::before {
        content: "Your code here."
    }

    .exercise {  /* green */
        background-color: rgb(225, 241, 223);
        border-color: rgba(91, 116, 127, 0.25);
    }

   .exercise * {
      color: rgb(91, 127, 116);
   }

    .student-entry {
        max-width: var(--max-width);
        padding: 16px 10px;
        border: 1px solid;
        border-radius: 6px;
        line-height: var(--lineHeight);

    }

   .exercise > .student-entry, .exercise > * > li > .student-entry {
        background-color: rgb(205, 221, 203);
        border-color: rgba(91, 116, 127, 0.25);
   }

    .info {  /* blue */
        background-color: rgb(210, 234, 244);
        border-color: rgba(91, 116, 127, 0.25);
    }
       .info * {
        color: rgb(91, 116, 127);
    }

    
    .assignment {  /* yellow */
        background-color: #FBE3BB;
        border-color: #EBDDBF;
    }
   .assignment * {
     color: #AF704D;
   }

    .assignment > .student-entry, .assignment > * > li > .student-entry {
        background-color: rgba( 150, 0, 0, 0.1);
        border-color: #AF704D;
    }

    .warning {  /* red */
        color: rgb(139, 83, 88);
        background-color: rgb(238, 213, 217);
        border-color: rgba(139, 83, 88, 0.25);
    }


    .addendum {
        background-color: DarkSalmon;
        color: White;
        font-size: 20px;
        font-weight: bold;
        height: 60px;
        padding-left: 20px;  
        padding-top: 55px !important;      
    }


    .todo {
        background-color: GoldenRod;
        color: DarkRed;
        font-size: 30px;
        font-weight: bold;
        padding-left: 20px;
        padding-bottom: 55px !important;      
        padding-top: 55px !important;      
    }

    .todo-next-year {
        background-color: Gray;
        color: Black;
        font-size: 30px;
        font-weight: bold;
        padding-bottom: 27px !important;      
        padding-left: 20px;  
        padding-top: 27px !important;      
    }
   
    .todo-description {
        font-size:12pt; 
        font-weight: normal;
    }


    /* Code fences */
    pre code {
    
    }

    /* Code block */
    .code {
        color: rgb(18, 18, 18);
        background-color: rgba(250, 250, 250, 0.75); /* gray background */
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: "Courier New", Courier, monospace;
        white-space: pre-wrap; /* Instead of using break tags for every individual line break, you can simply use newline characters. (However, for double line breaks, a break tag is still necessary, although a single one would suffice.) */
    }

    .codebox {
        padding-top: 0px;
        padding-bottom: 20px;
        padding-left: 15px;
        padding-right: 15px;
        color: rgb(18, 18, 18);
        background-color: rgba(250, 250, 250, 0.75); /* gray background */
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: "Courier New", Courier, monospace;
        white-space: pre-wrap; /* Instead of using break tags for every individual line break, you can simply use newline characters. (However, for double line breaks, a break tag is still necessary, although a single one would suffice.) */
    }



    details > div {
        padding-left: 15px;
        background-color: rgba(0, 0, 0, 0.05);
        padding: 15px;
        border-radius: 6px;
    }

    details > summary {
        cursor: pointer;
    }

    .quote {
        background: rgba(203, 195, 227);
        padding: 0.8em 10px;
        font-size: 1.05em;
        /*font-style: italic;*/
        line-height: 1.5em;
        color: rgb(123, 115, 147);
        border: 0 solid rgba(203, 195, 227, 0.8);  /* Width is overwritten via border-with */
        border-width: 1.5px 1.5px 1.5px 10px;
        border-radius: 4px;
        color: rgb(108, 60, 128);
        max-width: 500px;

    }

    .quote:before {
        content: "\“";
        font-size: 4em;
        line-height: 0.1em;
        margin-right: 0.25em;
        vertical-align: -0.4em;
        color: rgb(183, 175, 207);
    }

    .quote p {
        display: inline; 
    }


    .author {
        margin-top: 0.5em;
        color: rgb(123, 115, 147);
        font-style: normal;
        font-size: 0.8em;
    }


    /* ----- TEXT ----------------------------------------------------------- */

    p, li, h1, h2, h3, h4, h5, h6, pre {
      max-width: var(--max-width);
    }

    .rule-code{
        color:lightgray;
        font-size:11pt;
    }


    /* ----- TABLE -----------------------------------------------------------*/

    table {
        border-collapse: collapse;
        width: 100%;
    }

    th, td {
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
    }

    .clean-code {
        color: OliveDrab;
    }

    .dirty-code {
        color: IndianRed;
    }

</style>