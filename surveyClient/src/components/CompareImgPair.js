import React from 'react';

class CompareImgPair extends React.Component {

    constructor(props) {
        super()
        this.state = {
            httpLeft:props.leftHttp,
            httpRight:props.rightHttp
        }
    }

    componentWillReceiveProps(props) {
        this.setState({ 
            httpLeft:props.leftHttp,
            httpRight:props.rightHttp
        });  
      }

    render() {
        return (
            <fieldset >
                <div>
                    <div className="compareImgSet">
                        <img alt="image1" src={this.state.httpLeft}/>
                    </div>
                    <div className="compareImgSet">
                        <img alt="image2" src={this.state.httpRight}/> 
                    </div>
                </div>
            </fieldset>
        );
    }
}

export default CompareImgPair;