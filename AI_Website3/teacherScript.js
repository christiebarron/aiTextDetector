////1. read in data

//READ AND PROCESS THE STUDENT METADATA
let studentData = "../project3.json";


function essayPrint(id2, essay2){
  console.log(indivStudent.filter(o => o.student_name == id2 ))
  console.log(essay2)//indivStudent[id2]["essay"])
  var headingElement = document.getElementById("studentEssayToPrint")
  headingElement.textContent = essay2 // indivStudent[id2]["essay"]
}

//loop over and key-value pair.


//step 3: option change

function optionChanged(id){
  //buildCharts(id)
  intialProcess(id)
  console.log(id)
}

function option2Changed (id2){
  essayPrint(id2)
}



//STEP 1
function intialProcess(id) {
    //get data
    d3.json(studentData).then(function (data) {
      //create empty studentArray to eventually save name
      let studentArray = []
      let dict_test = {}
    
      //extract names
      for (let index = 0; index < data.length; index++){
          //save student name
        let studentName = data[index]["student_name"];
        //add student name to array of student names
        studentArray.push(studentName)
       }
      //print array to check that worked
      console.log(studentArray)
  
      //create drop-down menu for the student name selection
      let namesSelect = d3.select("#selDataset");
  
      //append the student name to the drop-down
      for (let index = 0; index < studentArray.length; index++) {
        const element = studentArray[index];
  
        // Append the text id, add a property to it. (WHAT IS THIS DOING?)
        namesSelect.append("option").text(element).property("value", element);
      }

      //create drop-down menu for the essay selection for given student
      let essaySelect = d3.select("#selEssay");

      //save indivStudent as global variable so can be called by subsequent functions
      globalThis.indivStudent = data.filter(o => o.student_name == id )
      //check that this worked 
      console.log(indivStudent)

     //reset essaySelect so only contains current student (not previous)
      essaySelect = essaySelect.html("")
       //append student essay to dropdown.
      for (let index = 0; index < indivStudent.length; index++) {
        const element1 = indivStudent[index].essay_set
        console.log(element1)

        // Append the text id, add a property to it. (WHAT IS THIS DOING?)
        essaySelect.append("option").text(element1).property("value", element1)
      }
      essayPrint(id, essay)
      //let essayPrint = indivStudent.filter(o => o.essay_set == element1)
    }
  )
}  






intialProcess ('Leora Roakes')
// essayPrint(id2)
// optionChanged(id)
// option2Changed(id2)

  