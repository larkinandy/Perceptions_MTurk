import React from 'react';
import '../componentstyle/App.css';
import $ from "jquery";
import rangeslider from 'rangeslider.js';

class CompareSlider extends React.Component {

    state = {value: "50",backgroundString: `linear-gradient(
        90deg,
        #D3D3D3 0%,
        #D3D3D3 100%
        )`}

    componentDidMount() {
        this.setState({onSliderChange: this.props.onSliderChange,shouldUpdate:this.props.shouldUpdate});
    }

    updateBackgroundString = (targetVal) =>  {
        const adjGradient = targetVal;
        const adjEndGradient =targetVal -1;
        if(targetVal<50) {
            this.setState({backgroundString: `linear-gradient(
                90deg,
                #D3D3D3 `+ adjGradient.toString() + `%,
                rgba(30,144,255,1.0) ` + adjEndGradient.toString() + `%,
                rgba(30,144,255,0.5) 50%,
                #D3D3D3 51%
                )`})
        }
        else {
            this.setState({backgroundString: `linear-gradient(
                90deg,
                #D3D3D3 49%,
                rgba(30,144,255,0.5) 50%,
                rgba(30,144,255,1.0) ` + adjEndGradient.toString() + `%,
                #D3D3D3 `+ adjGradient.toString() + `%
                )`})
        }
    }

    onSliderChange = event => {
        this.setState({value:event.target.value});
        this.props.onChange(event.target.value);
        
        this.updateBackgroundString(event.target.value);
    }

    componentWillReceiveProps(props) {
        if(props.shouldUpdate !==this.state.shouldUpdate) {
            this.updateBackgroundString(props.sliderVal);
            this.setState({
                value: props.sliderVal, 
                shouldUpdate: props.shouldUpdate
        })
        }
    }

    render() {
        return(
            <div className="range-slider">
                <input type="range" className="rs-range" 
                value={this.state.value} min="1" max="99" 
                onChange={this.onSliderChange}
                style={{background: this.state.backgroundString}}
                />
            </div>
        );
    }
};

export default CompareSlider