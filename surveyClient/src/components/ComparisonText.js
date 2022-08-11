import React from 'react';
import CompareSlider from './CompareSlider';

class ComparisonText extends React.Component {
   
    constructor(props) {
      super()
      this.state = {
        label:props.label,
        sliderVal:props.sliderVal,
        strengthLeft: '',
        strengthRight:'',
        leftBold:false,
        rightBold:false,
        number:props.number,
        passSliderVal:props.passSliderVal,
        grammar: props.grammar,
        shouldUpdate:props.shouldUpdate,
        textColor:props.textColor
      }
    }

    componentDidUpdate() {
    }

    componentWillReceiveProps(props) {
      if(props.shouldUpdate !==this.state.shouldUpdate) {
      this.setState({label:props.label,
        sliderVal:props.sliderVal,
        strengthLeft: '',
        strengthRight:'',
        leftBold:false,
        rightBold:false,
        number:props.number,
        passSliderVal:props.passSliderVal,
        grammar: props.grammar,
        shouldUpdate: props.shouldUpdate,
        textColor:props.textColor
      })
    }
    }

    onSliderChange = newSliderVal => {
        console.log(this.state.textColor);
        this.setState({sliderVal:newSliderVal});
        var strength = "slightly";
        if(newSliderVal < 16 || newSliderVal > 84) strength="much";
        else if(newSliderVal <33 || newSliderVal > 67) strength="moderately";
        if(newSliderVal < 50) {
			this.setState({strengthLeft:strength,strengthRight:'',leftBold:true,rightBold:false});
			}
			else if(newSliderVal >50){
				this.setState({strengthLeft:'',strengthRight:strength,leftBold:false,rightBold:true});
			}
        this.state.passSliderVal(newSliderVal);
    }

    render() {
        return(
            <fieldset><p className = "boldQuestion"> {this.state.number}. Which street {this.state.grammar} {this.props.label}? </p>
				<p style={{color:this.state.textColor}}>    Move the slider left or right to make your choice.  Move the slider farther if you feel more strongly about your choice.  You cannot rank the images as equal.</p>
				<div className="container">
					<span className="rangeText" id="q1LText"
						style={ this.state.leftBold ? { fontSize: 20-this.state.sliderVal/10} : { fontWeight: 'normal'} }
						//left street {this.state.grammar} <strong> {this.state.strengthLeft} </strong> {this.state.label}</span>
					>
						left street {this.state.grammar} {this.state.label}
					</span>
					<CompareSlider sliderVal = {this.state.sliderVal} onChange={this.onSliderChange} shouldUpdate={this.state.shouldUpdate}/>  
					<span className="rangeText" id="q1RText"
						style={ this.state.rightBold ? { fontSize: 20 - (100-this.state.sliderVal)/10} : { fontWeight: 'normal' } }
						//right street {this.state.grammar} <strong> {this.state.strengthRight} </strong> {this.state.label}</span>
					> right street {this.state.grammar} {this.state.label}
					</span>        
				</div>
            
			</fieldset>
        )
    }
}

export default ComparisonText;