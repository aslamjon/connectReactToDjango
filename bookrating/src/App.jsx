import React from 'react';
import './App.css';

class App extends React.Component {
  constructor() {
    super();

    this.state = {
      books: "",
      setBook: [],
    }
  }
  
  componentDidMount() {
  }

  componentDidMount() {
    // this.setState({books: "hel"})
    const fetchres = async() =>{
      const fet = await fetch("http://192.168.1.125:8000/student/", {
        method: "GET",
        headers: {
          "Content-type": "application/json",
        }
      });
      const res = await fet.json();
      this.setState({setBook: res})
      return res;
    }
    fetchres();
  }
  
  
  render() {

    console.log(this.state, "Render");
    return (
      <div className="App">
      <header className="App-header">
        {this.state.books}
        {this.state.setBook.map(elem => {
          return <span>{elem.id} {elem.name}</span>
        })}
      </header>
    </div>
    );
  }
}

export default App;
