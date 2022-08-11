import React from 'react';
import ComparisonText from './ComparisonText';
import CompareImgPair from './CompareImgPair';


class ComparisonDiv extends React.Component {

    constructor(props) {
        super();
        this.state = {
            paddingType: props.vals.paddingType,
            number: props.vals.number,
            label:props.vals.label, 
            leftHttp: props.vals.httpLeft,
            rightHttp: props.vals.httpRight,
            sliderVal: props.vals.sliderVal,
            returnSliderVal: props.vals.updateSliderVal,
            grammar: props.vals.grammar,
            shouldUpdate: props.vals.shouldUpdate,
            textColor: props.vals.textColor
        };
    }

    componentDidMount() {
    }

    componentDidUpdate() {
    }

    componentWillReceiveProps(props) {
        if(props.vals.shouldUpdate !== this.state.shouldUpdate) {
        this.setState({paddingType: props.vals.paddingType,
            number: props.vals.number,
            label:props.vals.label, 
            leftHttp: props.vals.httpLeft,
            rightHttp: props.vals.httpRight,
            sliderVal: props.vals.sliderVal,
            returnSliderVal: props.vals.updateSliderVal,
            grammar: props.vals.grammar,
            shouldUpdate: props.vals.shouldUpdate,
            textColor: props.vals.textColor
        })
      }
    }


    getSliderVal = (newSliderVal) => {
        this.state.returnSliderVal(this.state.number,newSliderVal);
    }

    render() {
        return(
            <div className = {this.state.paddingType} >
                <ComparisonText number ={this.state.number} label={this.state.label} passSliderVal={this.getSliderVal} sliderVal = {this.state.sliderVal} shouldUpdate = {this.state.shouldUpdate} grammar={this.state.grammar} textColor = {this.state.textColor}/>
                <CompareImgPair leftHttp={this.state.leftHttp} rightHttp={this.state.rightHttp}/>
            </div>
        );
    }
}


export default ComparisonDiv;