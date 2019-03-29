import React, { Component } from 'react';
import { withStyles, MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import styleApp from './styleApp.jsx';
import Fab from '@material-ui/core/Fab';
import CameraAlt from '@material-ui/icons/CameraAlt';
import blue from '@material-ui/core/colors/blue';
import { Player } from 'video-react';
import "../node_modules/video-react/dist/video-react.css"; 

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
        image: null
    };
}

  getPhoto() {
        fetch('http://172.26.215.47:8000/takephoto', { method: 'GET',
        mode: 'no-cors',}).then((response) => {
          console.log(response);
          this.setState({image: response});
          alert("response");
        }).catch((e) => {
          alert("deu pau")
        });
  }

  render() {
    const theme = createMuiTheme({
      palette: {
        primary: blue,
      },
      typography: {
        useNextVariants: true,
      },
      fab: {
        position: 'absolute',
        bottom: '15px',
        right: '15px',
      },
    });
    const { classes } = this.props;
    return (
      <div className={classes.App}>
        {/*<div className={classes.videoContainer}>
          <Player
            playsInline
            className={classes.video}
            poster="/assets/poster.png"
            src="http://172.26.250.145:8000/video_feed"
          />
    </div>*/}
        <div className={classes.imageContainer}><img className={classes.image} src="http://172.26.215.47:8000/video_feed"></img></div>
        <img src={this.state.image}>
          
        </img>
        <div className={classes.buttonContainer}>
          <MuiThemeProvider theme={theme}>
            <Fab color="primary" className={classes.fab} onClick={() => this.getPhoto()}>
              <CameraAlt />
            </Fab>
          </MuiThemeProvider>
        </div>
      </div>
    );
  }
}

export default withStyles(styleApp)(App);

