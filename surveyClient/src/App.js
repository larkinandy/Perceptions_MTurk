import React from 'react';
import './componentstyle/App.css';
import axios from 'axios';
import MainInstructions from './components/MainInstructions';
import ComparisonDiv from './components/ComparisonDiv';
import SubmitButton from './components/SubmitButton';

class App extends React.Component {

    state = {
        paddingTypes: ["bottomPad",'bottomPad','bottomPad','bottomPad','notBottomPad'],
        numbers: ['1','2','3','4','5'], 
        label: ['safer','more beautiful','more relaxing','more refreshing'],
        httpLeft: ['','','',''],
        httpRight: ['','','',''],
        sliderVals: ['50','50','50','50','50'],
        idsLeft: ['','','',''],
        idsRight: ['','','',''],
        grammar: ['is','is','is','is'],
        shouldUpdate:false,
        angle:'none'
    }

    componentDidMount() {
        this.onSearchSubmit();
    }

    passParams(num) {
        return({
            paddingType: this.state.paddingTypes[num],
            number: this.state.numbers[num],
            label: this.state.label[num],
            httpLeft: this.state.httpLeft[num],
            httpRight: this.state.httpRight[num],
            updateSliderVal: this.updateSliderVals,
            sliderVal: this.state.sliderVals[num],
            grammar: this.state.grammar[num],
            shouldUpdate:this.state.shouldUpdate
        });
    }

    updateSliderVals = (indexNum,newSliderVal) => {
        let updatedSliderVals = [...this.state.sliderVals];
        updatedSliderVals[indexNum-1] = newSliderVal;
        this.setState({sliderVals:updatedSliderVals});
    }

    getResults() {
        console.log("getting results");
    }

    async onSearchSubmit() {
        const response = await axios.get('https://shl-mt-backend.herokuapp.com/sample');
        this.setState(
            {
                label: response.data.labels,
                httpLeft: response.data.httpLeft,
                httpRight: response.data.httpRight,
                idsLeft: response.data.idLeft,
                idsRight: response.data.idRight,
                grammar: response.data.grammar,
                angle: response.data.angle,
                shouldUpdate:!this.state.shouldUpdate
            }
        )
    }

    formatResultsToJson = () => {
        let dataToSend = {
            labels:this.state.label,
            idsLeft:this.state.idsLeft,
            idsRight:this.state.idsRight,
            votes:this.state.sliderVals,
            angle:this.state.angle
        }
        return(dataToSend);
    }

    async sendResults(resultsToSend) {
        console.log("sending results");
        let dataToSend = this.formatResultsToJson();
        const response = await axios.post
        (
            'restfulServer/submit',
            dataToSend
        )
    }

    onButtonClick = () => {
        this.setState({label: ['a','b','c','d','e'],sliderVals: ['50','50','50','50','50'],shouldUpdate:!this.state.shouldUpdate});
        let results = this.getResults();
        this.sendResults(results);
        this.onSearchSubmit();
    }

  

    render = () => {
        return(
            <div className="container">
                <div className="row col-xs-12 col-md-12">
                    <div className="panel panel-primary">
                    <div className="panel-heading"><strong>Explanation of Research </strong>
                    </div>
                    <MainInstructions />
                    <div className="panel-heading"><strong>Instructions</strong></div>
                    <div className="panel-body">
                        <section>
                            <ComparisonDiv vals = {this.passParams(0)}/>
                            <ComparisonDiv vals = {this.passParams(1)}/>
                            <ComparisonDiv vals = {this.passParams(2)}/>
                            <ComparisonDiv vals = {this.passParams(3)}/>
                            <ComparisonDiv vals = {this.passParams(4)}/>
                        </section>
                    </div>
                    </div>
                    <SubmitButton onClick={this.onButtonClick}/>
                </div>
            </div>
        );
    }
};

export default App;