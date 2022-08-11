import React from 'react';
import '../componentstyle/App.css';

class MainInstructions extends React.Component {

    render() {
        return(
                    <div className="panel-body">
                        <p> <b> Project title:</b> Perceptions of the Built Environment <br/>
	                    <b> Principal Investigator: </b> Perry Hystad <br/>
                        <b> Co-investigator:  </b>  Andrew Larkin  <br/>
                        <b> Version Date: </b>	March 27, 2020 <br/>
                        </p>

                        <p> You are being asked to take part in a research study.  
                            The purpose of this research study is to gather participant perceptions of various environments using images from Google street view. 
                            Study activities include ranking images from Google street view.  
                            You will be paid $0.10 for being in this research study. 
                            You must be 18 years of age or older to participate.  
                            Your participation in this study is anonymous.  
                            While participation in this study is voluntary, all questions must be answered to be included in study results.  
                            If you have any questions about this research project, please contact: Perry Hystad at <a href="mailto:Spatial.Health.Lab@gmail.com?Subject=AMT%Survey" target="_top">Spatial.Health.Lab@gmail.com</a>. 
                            If you have questions about your rights or welfare as a participant, please contact the Oregon State University Institutional Review Board (IRB) Office, at (541) 737-8008 or by email at <a href="mailto:IRB@oregonstate.edu?Subject=AMT_Hystad%Survey" target="_top">IRB@oregonstate.edu</a>.</p>
	
                    </div>
        );
    }
};

export default MainInstructions