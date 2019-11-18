

========================================================================================================================================
 <div  id="mychats" style="width: 100%; max-width: 400px; height: 400px; overflow-x: scroll ; border-top: white solid 1px;">
                                  

 <q-chat-message
 v-for="item in CHATS"
 :name="item.name"
 :avatar="item.avatar"
 :text="item.message"
 :stamp="item.stamp"
 :sent = "item.sent"
 :bg-color="item.bg_color"
></q-chat-message>
      // Split in characters



  
<!-- 
<q-chat-message
 name="Jane"
 avatar="https://cdn.quasar.dev/img/avatar5.jpg"
 :text="[
   'doing fine, how r you?',
   'I just feel like typing a really, really, REALY long message to annoy you...'
 ]"
 size="6"
 stamp="4 minutes ago"
 text-color="white"
 bg-color="primary"
></q-chat-message>
<q-chat-message
 name="Jane"
 avatar="https://cdn.quasar.dev/img/avatar5.jpg"
 :text="['Did it work?']"
 stamp="1 minutes ago"
 size="8"
 text-color="white"
 bg-color="primary"
></q-chat-message> -->


   

 </div>
 <div class="row" style="width: 100% ">

   <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"> 
   <q-input v-on:keypress.enter.prevent="send_chat" style="width: 100% ;  margin-top: 20px;; background-color:white; color: #273746;" v-model="message" outlined  label="Enter your message"   >

 
     <template v-slot:after style="background-color: #273746;">
       <q-btn  dense  style="color:white; width: 150px; background-color: red;"  icon="send"  label="send"  @click="send_chat" ></q-btn>
     </template>
   </q-input>

 </div>


<div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">
   <q-btn round dense flat style="color:  white;; margin-top: 30px;;;" icon="send" @click="send_chat" ></q-btn>
 </div> 
      



   setInterval(this.updateScroll,1000);
   setInterval(() => {
    this.get_length()
   }, 2000);



 get_length(){
  var myuser = '{{user}}'
 
  axios.get(`${this.global_hostname}/api/CHAT_BOOTS_FOR_DELIBERATION/`)
  .then(res => {
    console.log(res)
    var data = res.data
   
    if(data.length > this.lengthofchats){
      this.lengthofchats = data.length

            if(this.CHATS.length <= 0){
             
              var temp =  data.filter((element)=>{return parseInt(element.evaluation_sheet) == this.GlobaEvaluationId })
              console.log(temp + '==================================f')
              var chats_temp = []
              for (let index = 0; index < temp.length; index++) {
                const element = temp[index];
             
                if(element.who.toLowerCase() == myuser.toLowerCase() ){
                  
                        
                        if(chats_temp.length <= 0 ){

                          var obj = {
                                    
                                    name : 'You',
                                    avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
                                    message : [element.messages],
                                    stamp : '7 minutes ago',
                                    sent : true,
                                    bg_color:'primary'           

                              
                              }
                              chats_temp.push(obj)


                        }else{
                            if(chats_temp[(chats_temp.length-1)].name.toLowerCase() == myuser.toLowerCase()){
                              chats_temp[(chats_temp.length-1)].message.push(element.messages)
                            }else{

                                
                                    var obj = {
                                        
                                        name : 'You',
                                        avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
                                        message : [element.messages],
                                        stamp : '7 minutes ago',
                                        sent : true,
                                        bg_color:'primary'           

                                  
                                  }
                                  chats_temp.push(obj)

                            }


                        }
                }else{

                   
                        
                              if(chats_temp.length <=0){

                                      var obj = {
                                          
                                          name : element.who,
                                          avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
                                          message : [element.messages],
                                          stamp : '7 minutes ago',
                                          sent : false,
                                          bg_color:'green-5'           

                                    
                                    }
                                    chats_temp.push(obj)


                              }else{

                              if(chats_temp[(chats_temp.length-1)].name.toLowerCase() == element.who){
                              chats_temp[(chats_temp.length-1)].message.push(element.messages)
                            }else{

                                
                                    var obj = {
                                        
                                        name : element.who,
                                        avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
                                        message : [element.messages],
                                        stamp : '7 minutes ago',
                                        sent : false,
                                        bg_color:'green-5'           

                                  
                                  }
                                  chats_temp.push(obj)

                            }




                              }

                }

                if(index == temp.length - 1 ){
                  this.CHATS = chats_temp
                }
                     
              
                


                
              }
            }else{
              this.recieved(data.filter((element)=>{return parseInt(element.evaluation_sheet) == this.GlobaEvaluationId }))
            }
     
    } 

  })
  .catch(err => {
    console.error(err); 
  })

},



updateScroll(){
var element = document.getElementById("mychats");
element.scrollTop = element.scrollHeight;

},





recieved(data){
  console.log('recice')
  console.log(data )
  var newdata = data

       
  var myuser = '{{user}}'


  if(this.CHATS[(this.CHATS.length-1)].name.toLowerCase() == newdata[(newdata.length-1)].who.toLowerCase() && newdata[(newdata.length-1)].who.toLowerCase() != myuser.toLowerCase()){
    this.CHATS[(this.CHATS.length-1)].message.push(newdata[(newdata.length-1)].messages)
  }else{

    if ( newdata[(newdata.length-1)].who.toLowerCase() != myuser.toLowerCase()) {
      

      
      var obj = {
                
                name : newdata[(newdata.length-1)].who,
                avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
                message : [newdata[(newdata.length-1)].messages],
                stamp : '7 minutes ago',
                sent : false,
                bg_color:'green-5'           

          
          }
          this.CHATS.push(obj)
         
    }
        


    
   


  }
},

send_chat(){
 
  if(this.CHATS.length >0){

    var myuser = '{{user}}'
  console.log(this.CHATS[(this.CHATS.length-1)])
if(this.CHATS[(this.CHATS.length-1)].name.toLowerCase() == myuser.toLowerCase()){

  this.CHATS[(this.CHATS.length-1)].message.push(this.message)
  this.message = ''

}else{
  
  var obj = {
   
               name : 'You',
               avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
               message : [this.message],
               stamp : '7 minutes ago',
               sent : true,
               bg_color:'primary'           

             
  }
  this.CHATS.push(obj)
  

}

var user = '{{ user }}'

var payload = {
  "evaluation_sheet": this.GlobaEvaluationId,
  "messages": this.message,
  "who": user,
  "avatar": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcREgqNXrVLOvypD9ErW3KpeyTA79C8K7C43v3V13d15lrFljEEf",

}

console.log(payload)
axios.post(`${this.global_hostname}/api/CHAT_BOOTS_FOR_DELIBERATION/`,payload,{
 
   headers: {
         'Content-Type': 'application/json',
          'X-CSRFToken': this.token
   }
  
})
.then(res => {
  console.log(res)

  this.message = ''
})
.catch(err => {
  console.error(err); 
})
  // var obj_message = {
  
  //                   name : 'Szhane',
  //                   avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
  //                   message : ,
  //                   stamp : '7 minutes ago',
  //                   sent   : false,
  //                   bg_color:'green-5'
               

  // }

  }else{

    var obj = {
            
            name : 'You',
            avatar : 'https://cdn.quasar.dev/img/avatar3.jpg',
            message : [this.message],
            stamp : '7 minutes ago',
            sent : true,
            bg_color:'primary'           

          
    }
    this.CHATS.push(obj)

  }
},

=============================================================================================
dialog fullscreen
<template>
  <div class="q-pa-md q-gutter-sm">
    <q-btn label="Maximized" color="primary" @click="dialog = true" />

    <q-dialog
      v-model="dialog"
      persistent
      :maximized="maximizedToggle"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <q-card class="bg-primary text-white">
        <q-bar>
          <q-space ></q-space>

          <q-btn dense flat icon="minimize" @click="maximizedToggle = false" :disable="!maximizedToggle">
            <q-tooltip v-if="maximizedToggle" content-class="bg-white text-primary">Minimize</q-tooltip>
          </q-btn>
          <q-btn dense flat icon="crop_square" @click="maximizedToggle = true" :disable="maximizedToggle">
            <q-tooltip v-if="!maximizedToggle" content-class="bg-white text-primary">Maximize</q-tooltip>
          </q-btn>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
          </q-btn>
        </q-bar>

        <q-card-section>
          <div class="text-h6">Alert</div>
        </q-card-section>

        <q-card-section>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum repellendus sit voluptate voluptas eveniet porro. Rerum blanditiis perferendis totam, ea at omnis vel numquam exercitationem aut, natus minima, porro labore.
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

dialog: false,
maximizedToggle: true


=========================================================================================================================

 <canvas id="myChart" width="400" height="200"></canvas>

      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June','July','August','September','October','November','December'],
              datasets: [{
                  label: 'Evaluation Per Year',
                  data: [12, 19, 3, 5, 2, 3],
                  fill : false,
                  backgroundColor: 'rgb(192, 57, 43)'
                      
                  ,
                   borderColor: 'rgb(192, 57, 43)',
                     
                 
                  borderWidth: 1
              }]
          },
          options: {
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      }
                  }]
              }
          }
      });

      
      ---------------------------------------------------------------------------------------------------------------------------------------
filterType : function(){
  // this.ViolationDepartmentPerCriteria_data
  var info = this.modelfiltertype
  this.ViolationDepartmentPerCriteria_data = this.VIOLATIONDINCOPY
  this.data = this.ViolationDepartmentPerCriteria_data
  if(info.toLowerCase() != 'no filter'){
     var data = this.VIOLATIONDINCOPY.filter(
         (element)=>{
          return element.Type.toLowerCase() == info.toLowerCase()
         }
     )
     alert(data)
     this.ViolationDepartmentPerCriteria_data = data
     this.data = this.ViolationDepartmentPerCriteria_data
  }


  // carulasan
  
 },

-----------------------------------------------------------

var a =this.CHOICESRAW
if(this.modelfilterminorgrave != "All"){
  
                // console.log(this.CHOICESRAW)
            
                var info = this.CHOICESRAW
                var data = info.filter(
                    (element)=>{
                        return element.graveofminor.toLowerCase().includes(this.modelfilterminorgrave.toLowerCase())
                        
                    }
                 )

                    // console.log(this.CHOICESRAW)
                this.violations_choices = data
           
    }else{
        this.violations_choices = this.CHOICESRAW
    }
-0--------------------------------------------------------------
this.$refs.jobstatus.validate()
                this.$refs.jobdescription.validate()
                   if (this.$refs.jobstatus.hasError || this.$refs.jobdescription.hasError ) {
                    this.formHasError = true
                        return
                 }else{
                  
                      var re = /^[A-Za-z]+$/;
                      if (re.test(this.jobstatus) && re.test(this.jobdescription)) {
                      

                        
            

                      }else{
                        
                        this.$q.notify({ //put dollor sign(q)
                                    message: `Numbers Not Allowed`,
                                    timeout: 3000, // in milliseconds; 0 means no timeout

                                    color: 'red',
                                    textColor: 'white', // if default 'white' doesn't fit
                                  icon: 'error', //or  avatar: 'statics/boy-avatar.png',

                                  position: 'top', // 'top', 'left', 'bottom-left' etc.

                                  })

                  
                          return

                      }


                 }

-------------------------------------------------------------------------



var check = this.Existingjostatus.filter(
  (element)=>{
    return element.toLowerCase() == this.jobstatus.toLowerCase()
  }
)
if(check.length > 0){
                this.$q.notify({ //put dollor sign(q)
message: `Oops! Already Exits Please Try Again`,
timeout: 3000, // in milliseconds; 0 means no timeout

color: 'red',
textColor: 'white', // if default 'white' doesn't fit
icon: 'pan_tool', //or  avatar: 'statics/boy-avatar.png',

position: 'top', // 'top', 'left', 'bottom-left' etc.

})


  return
}





------------------------------------------------------
date split
<template>
  <div>
    <q-splitter
      v-model="splitterModel"
      style="height: 450px"
    >

      <template v-slot:before>
        <div class="q-pa-md">
          <q-date
            v-model="date"
            :events="events"
            event-color="orange"
          />
        </div>
      </template>

      <template v-slot:after>
        <q-tab-panels
          v-model="date"
          animated
          transition-prev="jump-up"
          transition-next="jump-up"
        >
          <q-tab-panel name="2019/02/01">
            <div class="text-h4 q-mb-md">2019/02/01</div>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
          </q-tab-panel>

          <q-tab-panel name="2019/02/05">
            <div class="text-h4 q-mb-md">2019/02/05</div>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
          </q-tab-panel>

          <q-tab-panel name="2019/02/06">
            <div class="text-h4 q-mb-md">2019/02/06</div>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>
          </q-tab-panel>
        </q-tab-panels>
      </template>
    </q-splitter>
  </div>
</template>


---------------------------------------------------

<template>
  <div class="q-pa-md" style="max-width: 350px">
    <q-list bordered>
      <q-expansion-item
        group="somegroup"
        icon="explore"
        label="First"
        default-opened
        header-class="text-primary"
      >
        <q-card>
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-separator />

      <q-expansion-item group="somegroup" icon="perm_identity" label="Second" header-class="text-teal">
        <q-card>
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-separator />

      <q-expansion-item group="somegroup" icon="shopping_cart" label="Third" header-class="text-purple">
        <q-card>
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>

      <q-separator />

      <q-expansion-item
        group="somegroup"
        icon="bluetooth"
        label="Fourth"
        header-class="bg-teal text-white"
        expand-icon-class="text-white"
      >
        <q-card class="bg-teal-2">
          <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
            commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
            eveniet doloribus ullam aliquid.
          </q-card-section>
        </q-card>
      </q-expansion-item>
    </q-list>
  </div>
</template>

/* <q-expansion-item
 group="somegroup"
 icon="fiber_manual_record"
 label="Performance Evaluation"
 default-opened
 style="color:red ;font-weight: 900; "
>
 <q-card>

 </q-card>
 </q-expansion-item>*/


-----------------------------------------------------------





// def index(request): 

        
        
// try: isay
//         sales = requests.get('https://kharizzapointofsale.000webhostapp.com/Sales.php/')  
//         pretty_json_sales = json.loads(sales.text) 

//         category = requests.get('https://kharizzapointofsale.000webhostapp.com/category.php/')  
//         pretty_json_category = json.loads(category.text) 

//         products = requests.get('https://kharizzapointofsale.000webhostapp.com/products.php/')  
//         pretty_json_products = json.loads(products.text)

//         r = requests.get('https://kharizzapointofsale.000webhostapp.com/TodaySales.php/')
//         pretty_json = json.loads(r.text)

// except Exception as e:
//         print('nag ka error')
//         reverse('index')


// context = {
//     'TodaySales' : json.dumps(pretty_json, indent=2),
//     'Products' : json.dumps(pretty_json_products,indent=2),
//     'Category' : json.dumps(pretty_json_category,indent=2),
//     'Sales' : json.dumps(pretty_json_sales,indent=2)
// }
// return 





--------------------------------------------------------------------------
 this.$q.notify({ //put dollor sign(q)
  message: `Successfully Updated!`,
  timeout: 3000, // in milliseconds; 0 means no timeout

  color: 'orange',
  textColor: 'white', // if default 'white' doesn't fit
icon: 'check', //or  avatar: 'statics/boy-avatar.png',

position: 'top', // 'top', 'left', 'bottom-left' etc.

})
////////////////////////////// OOPS already exists
this.$q.notify({ //put dollor sign(q)
  message: `Oops! Already Exits Please Try Again`,
  timeout: 3000, // in milliseconds; 0 means no timeout

  color: 'red',
  textColor: 'white', // if default 'white' doesn't fit
icon: 'pan_tool', //or  avatar: 'statics/boy-avatar.png',

position: 'top', // 'top', 'left', 'bottom-left' etc.

})

-----------------------------------------------------------------


// [
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/1/",
//       "id": 1,
//       "NameofUserLevel": "admin",
//       "EmployeePerformance": false,
//       "ReportsModule": true,
//       "PerformanceEvaluationModule": true,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": true,
//       "FileMaintenance_General": true,
//       "FileMaintenance_Accounts": true,
//       "FileMaintenance_EvaluationSheet": true,
//       "FileMaintenance_Departments": true,
//       "FileMaintenance_Offense": true,
//       "FileMaintenance_EvaluationGuide": true,
//       "FileMaintenance_PlaceofAssignment": true,
//       "FileMaintenance_JobLevelorAccessLevel": true,
//       "FileMaintenance_201File": true,
//       "DeliberationModule": true,
//       "CustomerConcern": true,
//       "date_created": "2019-09-29T12:22:56Z",
//       "date_updated": "2019-10-14T15:07:23.739341Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/2/",
//       "id": 2,
//       "NameofUserLevel": "supervisory",
//       "EmployeePerformance": false,
//       "ReportsModule": true,
//       "PerformanceEvaluationModule": true,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": false,
//       "CustomerConcern": false,
//       "date_created": "2019-09-29T12:23:52Z",
//       "date_updated": "2019-10-14T09:27:11.052206Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/3/",
//       "id": 3,
//       "NameofUserLevel": "managerial",
//       "EmployeePerformance": false,
//       "ReportsModule": false,
//       "PerformanceEvaluationModule": true,
//       "SystemDashboardModule": false,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": false,
//       "CustomerConcern": true,
//       "date_created": "2019-09-29T12:24:06Z",
//       "date_updated": "2019-09-29T12:24:06Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/4/",
//       "id": 4,
//       "NameofUserLevel": "DeliberationParticipant",
//       "EmployeePerformance": false,
//       "ReportsModule": false,
//       "PerformanceEvaluationModule": false,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": true,
//       "CustomerConcern": false,
//       "date_created": "2019-09-29T12:25:30Z",
//       "date_updated": "2019-09-30T15:35:05Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/5/",
//       "id": 5,
//       "NameofUserLevel": "AdminStaff",
//       "EmployeePerformance": false,
//       "ReportsModule": true,
//       "PerformanceEvaluationModule": false,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": true,
//       "FileMaintenance_General": true,
//       "FileMaintenance_Accounts": true,
//       "FileMaintenance_EvaluationSheet": true,
//       "FileMaintenance_Departments": true,
//       "FileMaintenance_Offense": true,
//       "FileMaintenance_EvaluationGuide": true,
//       "FileMaintenance_PlaceofAssignment": true,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": true,
//       "DeliberationModule": false,
//       "CustomerConcern": false,
//       "date_created": "2019-09-29T12:26:06Z",
//       "date_updated": "2019-09-29T12:26:06Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/6/",
//       "id": 6,
//       "NameofUserLevel": "LegalDepartment",
//       "EmployeePerformance": false,
//       "ReportsModule": false,
//       "PerformanceEvaluationModule": false,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": false,
//       "CustomerConcern": true,
//       "date_created": "2019-10-12T05:54:37Z",
//       "date_updated": "2019-10-12T05:59:50Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/7/",
//       "id": 7,
//       "NameofUserLevel": "CustomerService",
//       "EmployeePerformance": false,
//       "ReportsModule": false,
//       "PerformanceEvaluationModule": false,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": false,
//       "CustomerConcern": true,
//       "date_created": "2019-10-12T06:22:09Z",
//       "date_updated": "2019-10-12T06:22:09Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/8/",
//       "id": 8,
//       "NameofUserLevel": "CallCenter",
//       "EmployeePerformance": false,
//       "ReportsModule": false,
//       "PerformanceEvaluationModule": false,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": false,
//       "CustomerConcern": true,
//       "date_created": "2019-10-12T12:44:32Z",
//       "date_updated": "2019-10-12T12:44:32Z"
//   },
//   {
//       "url": "http://127.0.0.1:8000/api/AccessLevel/9/",
//       "id": 9,
//       "NameofUserLevel": "rank and file",
//       "EmployeePerformance": false,
//       "ReportsModule": false,
//       "PerformanceEvaluationModule": false,
//       "SystemDashboardModule": true,
//       "FileMaintenanceModule": false,
//       "FileMaintenance_General": false,
//       "FileMaintenance_Accounts": false,
//       "FileMaintenance_EvaluationSheet": false,
//       "FileMaintenance_Departments": false,
//       "FileMaintenance_Offense": false,
//       "FileMaintenance_EvaluationGuide": false,
//       "FileMaintenance_PlaceofAssignment": false,
//       "FileMaintenance_JobLevelorAccessLevel": false,
//       "FileMaintenance_201File": false,
//       "DeliberationModule": false,
//       "CustomerConcern": false,
//       "date_created": "2019-10-21T22:27:07.970045Z",
//       "date_updated": "2019-10-21T22:43:32.654178Z"
//   }
// ]


**888&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  

  // prof = profile.objects.get(account=user.id)
  // p = prof.empcode.lower()
  // employee = tbl_employee.objects.get(EmpCode=p)
  // print(f'adsfdsf {employee.JobLevel}')
  // if  'rank' in employee.JobLevel or 'Rank' in employee.JobLevel: 
      
      
  //     print(employee)
  //     print('randprint')
  //     JobLevel = employee.JobLevel.lower()
  //     request.session['JobLevel'] = employee.JobLevel
  //     request.session['fullname'] = employee.FirstName
  //     print(JobLevel)
  //     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=JobLevel)
  //     # get the modules
  //     request.session['empcode'] = employee.EmpCode
  //     request.session['ReportsModule'] = GetAccessModules.ReportsModule
  //     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
  //     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
  //     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
  //     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
  //     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
  //     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
  //     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
  //     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
  //     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
  //     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
  //     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
  //     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
  //     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
  //     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern


*****************************************************
//  var hostname = window.location.hostname;
//  var port = window.location.port
//  if(port != '' ){

//      hostname = hostname+':8000'
//  }
//  else{
//      hostname = hostname
//  }


// this.global_hostname = `${window.location.protocol}//${hostname}`
// var csrftoken = Cookies.get('csrftoken');
// this.token = csrftoken



*****************************************
/* <q-input v-model="password" filled :type="isPwd ? 'password' : 'text'" hint="Password with toggle">
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
 </q-input> */


*******************************************************************************
// this.$q.dialog({
//         title: 'Confirm',
//         message: 'Would you like to turn on the wifi?',
//         cancel: true,
//         persistent: true
//       }).onOk(() => {
//         // console.log('>>>> OK')
//       }).onOk(() => {
//         // console.log('>>>> second OK catcher')
//       }).onCancel(() => {
//         // console.log('>>>> Cancel')
//       }).onDismiss(() => {
//         // console.log('I am triggered on both OK and Cancel')
// })

***********************************************
// this.$q.notify({ //put dollor sign(q)
//   message: `Successfuly Saved!`,
//   timeout: 3000, // in milliseconds; 0 means no timeout

//   color: 'green',
//   textColor: 'white', // if default 'white' doesn't fit
// icon: 'check', //or  avatar: 'statics/boy-avatar.png',

// position: 'top', // 'top', 'left', 'bottom-left' etc.

// })


******************************************************************************
/* <q-dialog v-model="modal_qrcode" persistent>
  <q-card style="width: 900px; max-width: 1020;">
    <div id="printMe">
        <q-card-section  class="row items-center" style="padding: 30px; width: 100%;">
       
            <img width="150px;"  style="margin-left: auto;margin-right: auto;width: 50%" :src="qr" alt="QR" srcset="">
    
              <!-- buru -->
              
          </q-card-section>
          <q-item-label style="width: 100%; text-align: center; font-weight: bold;">
             ${ web_info_qr }
    
          </q-item-label>
    
      
    
    

    </div>
  
    <q-card-actions align="center">
        <q-btn push  label="Close" color="grey" v-close-popup ></q-btn>
      <q-btn push icon="print" @click="printna"  label="Print" color="red-8"  ></q-btn>
    </q-card-actions>
  </q-card>
</q-dialog> */



***************************************************
/* <q-item  style="width: 100%;" clickable tag="a"    >
            
            <q-item-section avatar>
              <q-icon   name="dashboard"></q-icon>
            </q-item-section>
            <q-item-section>
              <q-item-label>Actiivity Logs</q-item-label>
              
            </q-item-section>
  </q-item> */
***********************************************************************************************************
  // <q-item >
  //             <div style="width: 100%;">
  //                 <!-- <img :src="url" width="60" alt="logo"> -->
  //                 <div style="padding:10px; width: 100%;" id="logos">
  //                     <img style="padding : 20px; margin-left: 50px;" height="150" width="150" src="{% static 'img/logongvictory_final.PNG' %}" alt="">
  //                   </div>
  //               </div>       
  //         </q-item>


********************************************************
// python to javascrips
// def index(request): 
//     r = requests.get('https://kharizzapointofsale.000webhostapp.com/TodaySales.php/')
//     pretty_json = json.loads(r.text)
    
//     context = {
//             'TodaySales' : json.dumps(pretty_json, indent=2)
//     }
//   return render(request, 'index.html', context)

//   var json_string = unescape("{{TodaySales | safe | escapejs}}");
//         var json_data = JSON.parse(json_string);
//         console.log(json_data)

***************************************


// <!DOCTYPE html>
// <html lang="en">
// <head>
//   <meta charset="UTF-8">
//   <meta name="viewport" content="width=device-width, initial-scale=1.0">
//   <meta http-equiv="X-UA-Compatible" content="ie=edge">
//   <title>Document</title>

//   <!-- Do you need Material Icons? -->
//   <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons" rel="stylesheet" type="text/css">

//   <!-- Do you need Fontawesome? -->
//   <link href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" rel="stylesheet">

//   <!-- Do you need Ionicons? -->
//   <link href="https://cdn.jsdelivr.net/npm/ionicons@^4.0.0/dist/css/ionicons.min.css" rel="stylesheet">

//   <!-- Do you need MDI? -->
//   <link href="https://cdn.jsdelivr.net/npm/@mdi/font@^3.0.0/css/materialdesignicons.min.css" rel="stylesheet">

//   <!-- Do you need all animations? -->
//   <link href="https://cdn.jsdelivr.net/npm/animate.css@^3.5.2/animate.min.css" rel="stylesheet">


//   <!--
//     Finally, add Quasar's CSS:
//     Replace version below (1.0.3) with your desired version of Quasar.
//     Add ".rtl" for the RTL support (example: quasar.rtl.min.css).
//   -->
//   <link href="https://cdn.jsdelivr.net/npm/quasar@^1.0.3/dist/quasar.min.css" rel="stylesheet" type="text/css">


// </head>

// <body>

//   <!-- Do you want IE support? Replace "1.0.3" with your desired Quasar version -->
//   <script src="https://cdn.jsdelivr.net/npm/quasar@^1.0.3/dist/quasar.ie.polyfills.umd.min.js"></script>

//   <!-- You need Vue too -->
//   <script src="https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.min.js"></script>

//   <!--
//     Add Quasar's JS:
//     Replace version below (1.0.3) with your desired version of Quasar.
//   -->
//   <script src="https://cdn.jsdelivr.net/npm/quasar@^1.0.3/dist/quasar.umd.min.js"></script>

//   <!--
//     If you want to add a Quasar Language pack (other than "en-us").
//     Notice "pt-br" in "i18n.pt-br.umd.min.js" for Brazilian Portuguese language pack.
//     Replace version below (1.0.0-beta.0) with your desired version of Quasar.
//     Also check final <script> tag below to enable the language
//     Language pack list: https://github.com/quasarframework/quasar/tree/dev/ui/lang
//   -->
//   <script src="https://cdn.jsdelivr.net/npm/quasar@^1.0.3/dist/lang/pt-br.umd.min.js"></script>

//   <!--
//     If you want to make Quasar components (not your own) use a specific set of icons (unless you're using Material Icons already).
//     Replace version below (1.0.3) with your desired version of Quasar.
//     Icon sets list: https://github.com/quasarframework/quasar/tree/dev/ui/icon-set
//   -->
//   <script src="https://cdn.jsdelivr.net/npm/quasar@^1.0.3/dist/icon-set/fontawesome-v5.umd.min.js"></script>

//   <script>
//     // if using a Quasar language pack other than the default "en-us";
//     // requires the language pack style tag from above
//     Quasar.lang.set(Quasar.lang.ptBr) // notice camel-case "ptBr"

//     // if you want Quasar components to use a specific icon library
//     // other than the default Material Icons;
//     // requires the icon set style tag from above
//     Quasar.iconSet.set(Quasar.iconSet.fontawesomeV5) // fontawesomeV5 is just an example

//     /*
//       Example kicking off the UI.
//       Obviously, adapt this to your specific needs.
//      */

//     // custom component example, assumes you have a <div id="my-page"></div> in your <body>
//     Vue.component('my-page', {
//       template: '#my-page'
//     })

//     // start the UI; assumes you have a <div id="q-app"></div> in your <body>
//     new Vue({
//       el: '#q-app',
//       data: function () {
//         return {}
//       },
//       methods: {},
//       // ...etc
//     })
//   </script>
// </body>


// </html>



********************************************************************************


/* <q-table

     
style="width: 100%"
:data="data"
:columns="columns"
row-key="id"
selection="single"
:selected.sync="selected"
 :filter="terms"
    grid
    title="Evaluation "

>
<!-- hai -->

<template  slot="top-selection" >

            <!-- <div>
                <q-tooltip >
                Click to Evaluate
                </q-tooltip>
                <q-btn push class="animated fadeInDown" dense color="red-8" label="Start Evaluate"  icon="launch" @click="event_evaluate" ></q-btn>
                
            </div> -->
</template>



     <template v-slot:top-right>
  
     <div style="width: 100px; font-size: 15px; color: grey;">
                  <span>Filter</span>
                  <q-icon style="font-size: 25px;" name="filter_list"></q-icon>
              </div>


  <div style="width: 300px;padding: 10px;">
      <q-select  outlined   filled label="Type Of Evaluation" ></q-select>
      <!-- :options="options_terminal" -->
  </div>
  
  <div style="width: 200px;padding: 10px;">
      <q-select outlined   filled  label="Department" ></q-select>
      <!-- :options="options_department" -->
  </div> 
  <div style="width: 200px;padding: 10px;">
    <q-select outlined   filled  label="Criteria" ></q-select>
    <!-- :options="options_department" -->
</div> 
<q-input outlined  style="width: 200px;padding: 10px;"  filled  dense debounce="300"  placeholder="Search">
        <template v-slot:append>
          <q-icon name="search" ></q-icon>
        </template>
    </q-input>
  
  
  
  
 


       


 
  </template>



</q-table> */


// columns: [
          
//           {
//           name: 'desc',
//           required: true,
//           label: 'EmpCode',
//           align: 'left',
//           field: row => row.EmpCode,
//           format: val => `${val}`,
//           sortable: true
//         },
//         { name: 'FirstName', align: 'center', label: 'First Name', field: 'FirstName', sortable: true },
//         { name: 'MiddleName', align: 'center', label: 'Middle Name', field: 'MiddleName', sortable: true },
//         { name: 'LastName', label: 'Last Name', field: 'LastName', sortable: true },
//         { name: 'Suffix', label: 'Suffix', field: 'Suffix' },
//         { name: 'NickName', label: 'NickName', field: 'NickName' },
//         { name: 'JobLevel', label: 'Job Level', field: 'JobLevel' },
//         { name: 'JobStatus', label: 'Job Status', field: 'JobStatus' },
//         { name: 'Department', label: 'Department', field: 'Department', sortable: true },
//         { name: 'Designation', label: 'Designation', field: 'Designation', sortable: true },
//         { name: 'ContactNumber', label: 'ContactNumber', field: 'ContactNumber', sortable: true },
//       ],
//       data: [
               
//       ],
// selected : [],

// terms: ''



        

        

******************************************************************************************