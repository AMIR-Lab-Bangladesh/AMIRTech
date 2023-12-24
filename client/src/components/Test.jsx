import React from "react";
import Layout from "./Layout";
import bgvideo from "../assets/bg.mp4";

const Test = () => {
  return (
    <Layout>
      <div>
        <center>
          <h1>AMIR Innovative Technology</h1>
          <video className="bg-video-nn" autoPlay muted loop>
            <source src={bgvideo} type="video/mp4" />
          </video>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum voluptates facere vero eos ea? Aperiam at exercitationem nihil dolorem quod sed itaque. Deserunt doloribus ea natus commodi illum eligendi. Cum eligendi nesciunt fugit quos accusantium dolorem accusamus eveniet doloribus, fugiat molestiae quasi qui odio alias ullam officiis aliquam, error, tempora veniam repellendus voluptatem perferendis. Placeat eveniet rerum sequi dolore autem quidem sint? Excepturi perspiciatis iste doloribus beatae eum molestiae mollitia explicabo porro numquam quam blanditiis in sed quidem optio culpa quia id reprehenderit magni, eveniet voluptates quos assumenda quibusdam consequuntur. Expedita dolore, neque sunt repudiandae perspiciatis modi facere unde, a nemo voluptatum vitae eveniet officia. Nesciunt asperiores exercitationem libero accusantium laboriosam! Quidem impedit ab, commodi et vero sequi repudiandae provident incidunt itaque aliquam hic placeat quis minima saepe, eligendi excepturi! Voluptates dignissimos molestiae perferendis excepturi! Saepe ex eveniet blanditiis ducimus exercitationem repellat aliquid a suscipit rerum temporibus deleniti placeat obcaecati animi delectus nisi, facilis dolor vitae fugiat eum quis cum tempora id. A eveniet animi non doloremque, sit dolore incidunt eaque ratione aut similique placeat, aliquid, debitis doloribus explicabo. Doloribus sed modi non vero praesentium fugiat. Recusandae, hic odio suscipit culpa similique error qui esse placeat minima rem, exercitationem quaerat!</p>

          {/* <div className="bg-video-nn">Nice</div> */}
        </center>
      </div>
    </Layout>
  );
};

export default Test;
