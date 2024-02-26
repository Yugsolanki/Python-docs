import React from "react";
import styles from "./styles.module.css";

const Terminal = (props) => {
  const { commands } = props;
  return (
    <div className={styles.terminal}>
      <div>
        {commands.map((command, index) => (
          <div key={index} className={styles.command}>
            ```
            {command}
            ```
          </div>
        ))}
      </div>
    </div>
  );
};

export default Terminal;
