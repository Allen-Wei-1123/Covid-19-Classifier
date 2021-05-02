
import React,{Fragment} from 'react'; 
import ReactDOM from 'react-dom'; 
import axios from 'axios'
import  './App.scss'
class App extends React.Component {

  state = {
    msg:"",
    predicted:"",
    cnt:0
  }

  handleChange = e=>{
    this.setState({
      msg:e.target.value
    })
  }

  handlesubmit = e=>{
      axios.post('http://127.0.0.1:4455/submit',{
        msg : this.state.msg
      }).then((response)=>{
        console.log(response.data)
        this.setState({
          predicted:response.data,
          
        })
        this.setState(prev=>{
          return {cnt:prev.cnt+1}
        })
      },(error)=>{
        console.log(error)
      })

  }

  
  

  render(){
      return (
     
        <Fragment>
          <link rel="preconnect" href="https://fonts.gstatic.com"></link>
          <link rel="preconnect" href="https://fonts.gstatic.com"></link>
        <div className="App">
          <div className="textarea">
              <h1>
                Fake Covid-19 News Classifier
              </h1>
              <textarea id = "text" onChange={this.handleChange} >

              </textarea>
              <input id = "submit-btn"type = "submit" value = "Predict" onClick={this.handlesubmit}></input>
              <div id = "answer">
                {
                  this.state.predicted == 1 ? "Real News" : "Fake News"
                }
              </div>
          </div>
        </div>
        </Fragment>
      );
  }
}

export default App;
