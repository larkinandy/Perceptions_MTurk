import React from 'react';

class ErrMsg extends React.Component {

    constructor(props) {
        super()
        this.state = {
            errText: " "
        }
        console.log(props)
    }

    componentWillReceiveProps(props) {
        this.setState({
            errText:props.errMsg
        })
        console.log(this.state.errText);
      }

    render() {
        return(
            <div>
                <p className="err-msg">{this.state.errText}</p>
            </div>
        );
    }
}

export default ErrMsg;