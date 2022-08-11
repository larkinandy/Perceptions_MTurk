import React from 'react';

class SubmitButton extends React.Component {

    state = {onButtonClick:''};

    componentDidMount() {
        this.setState({
            onButtonClick:this.props.onButtonClick
        });
    };

    onButtonClick = event => {
        console.log(this.state);
        console.log(this.props);
        //event.preventDefault();
        this.props.onClick();
    }

    render() {
        return(
            <div>
                <button className="button" onClick={this.onButtonClick}>Submit</button>
            </div>
        );
    }
}

export default SubmitButton;